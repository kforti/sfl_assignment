from pathlib import Path
from typing import Dict

import pandas as pd


def local_csv_data_access_factory(config: Dict):
    data_access = LocalCSVDataAcess(config['base_path'])
    return data_access


class LocalCSVDataAcess:
    def __init__(self, base_path=None):
        self._base_path = base_path

    @property
    def base_path(self):
        if self._base_path is None:
            path = Path("")
        else:
            path = Path(self._base_path)
        return path

    def get(self, name):
        path = self.base_path.joinpath(name)
        records = pd.read_csv(path).to_dict(orient='records')
        return records


def s3_csv_data_access_factory(config: Dict):
    data_access = S3CSVDataAcess(bucket=config['bucket'],
                                 storage_options=config.get('storage_options'))
    return data_access


class S3CSVDataAcess:
    def __init__(self, bucket, storage_options=None):
        self.bucket = bucket
        self.storage_options = storage_options

    def get(self, name):
        url = Path(f"s3://{self.bucket}").joinpath(name)
        records = pd.read_csv(str(url), storage_options=self.storage_options).to_dict(orient='records')
        return records
