from colorama import Fore
from pathlib import Path
from .ultilities import make_dir


class DataPipeLine:
    def __init__(
            self,
            query: str,
            count_rows: bool = False,
            use_polars: bool = True,
    ):
        self.query = query
        self.use_polars = use_polars
        self.count_rows = count_rows
        self.status = f'{Fore.LIGHTBLUE_EX}🤖 JDBC:{Fore.RESET}'

        if self.count_rows:
            self.query = f"select count(*) from ({query})"

    def debug_query(self):
        print(self.query)

    def records_to_df(self, records, columns: list, save_path: Path):
        import pandas as pd
        import polars as pl

        if self.use_polars:
            df = pl.DataFrame(records, orient='row', schema=columns)
        else:
            df = pd.DataFrame(records, columns=columns)

        if save_path:
            make_dir(save_path.parent)
            if self.use_polars:
                df.write_parquet(save_path)
            else:
                df.to_parquet(save_path, index=False, compression='zstd')
        return df

    def run_presto_to_df(
            self,
            save_path: Path = None,
            verbose: bool = True,
    ):
        from concurrent.futures import ThreadPoolExecutor
        from time import sleep
        from datetime import datetime
        import trino
        import os
        from tqdm import tqdm

        # connection
        username, password = os.environ['PRESTO_USER'], os.environ['PRESTO_PASSWORD']
        conn = trino.dbapi.connect(
            host='presto-secure.data-infra.shopee.io',
            port=443,
            user=username,
            catalog='hive',
            http_scheme='https',
            source=f'(50)-(vnbi-dev)-({username})-(jdbc)-({username})-(SG)',
            auth=trino.auth.BasicAuthentication(username, password)
        )
        cur = conn.cursor()

        # verbose
        start = datetime.now()
        print(f"{self.status} Start to query {start.strftime("%Y-%m-%d %H:%M:%S")}")
        if verbose:
            thread = ThreadPoolExecutor(1)
            async_result = thread.submit(cur.execute, self.query)

            bar_queue = tqdm()
            while not async_result.done():
                memory = cur.stats.get('peakMemoryBytes', 0) * 10 ** -9
                perc = 0
                stt = cur.stats.get('state', '')
                if stt == "RUNNING":
                    perc = round((cur.stats.get('completedSplits', 0) * 100.0) / (cur.stats.get('totalSplits', 0)), 2)
                status = f"🤖 JDBC Status: {stt} {perc}%, Memory {memory:,.0f}GB"
                bar_queue.set_description(status)
                bar_queue.update(1)
                sleep(5)
            bar_queue.close()
        else:
            cur.execute(self.query)
        records = cur.fetchall()

        # result
        columns = [i[0] for i in cur.description]
        df = self.records_to_df(records, columns, save_path)

        if self.count_rows:
            print(f"{self.status} Count rows: {records[0][0]}")

        end = datetime.now()
        print(
            f"{self.status} Finish {end.strftime("%Y-%m-%d %H:%M:%S")} in "
            f"{(end - start).total_seconds():,.2f}s \n"
            f"{self.status} Data Shape: {df.shape}"
        )
        return df
