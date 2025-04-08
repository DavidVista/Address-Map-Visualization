import pandas as pd
import asyncio
from contextvars import copy_context, ContextVar
import json


class Scraper:
    # IP address and port of the server
    delivery_address: str = '127.0.0.1:500'
    # File name of the csv table
    dataset_name: str = 'ip_addresses'
    # Uploaded csv dataset
    dataframe: pd.DataFrame

    def _load_dataset(self) -> pd.DataFrame:
        try:
            with open(f'{self.dataset_name}.csv', 'r') as f:
                df = pd.read_csv(f)
                return df
        except OSError as e:
            print(f"Exception catched while working with file: {e.__str__()}")

    def _clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        cleaned_df = df.copy()

        # Data type convertion
        cleaned_df[['Longitude', 'Latitude']] = df[['Longitude', 'Latitude']].astype(pd.Float64Dtype())
        cleaned_df['Timestamp'] = df['Timestamp'].astype(pd.Int64Dtype())
        cleaned_df['suspicious'] = df['suspicious'].astype(pd.BooleanDtype())

        # Move timestamp to delay
        cleaned_df['Timestamp'] -= min(cleaned_df['Timestamp'])
        cleaned_df = cleaned_df.rename(columns={'Timestamp': 'delay'})

        return cleaned_df

    def _post_json(self, data: dict) -> None:
        print(f"Posting a json: {json.dumps(data)}\n\n")

    def __init__(self,
                 delivery_address: str = '127.0.0.1:500',
                 dataset_name: str = 'ip_addresses'):
        self.delivery_address = delivery_address
        self.dataset_name = dataset_name
        self.dataframe = self._clean_data(self._load_dataset())

    async def deliver_data(self):
        async with asyncio.TaskGroup() as tg:
            record_ctx_var = ContextVar('record')
            for i, record in enumerate(self.dataframe.to_dict(orient='records')):
                record_ctx_var.set(record)
                ctx = copy_context()
                task_i = tg.create_task(
                    asyncio.sleep(record['delay']),
                    context=ctx
                )
                task_i.add_done_callback(
                    lambda x: self._post_json(x.get_context()[record_ctx_var])
                )


if __name__ == "__main__":
    scraper = Scraper()
    asyncio.run(scraper.deliver_data())
