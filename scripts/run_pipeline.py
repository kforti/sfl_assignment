from pathlib import Path

import sqlalchemy
import pandas as pd

from sfl_assignment.models import Configuration
from sfl_assignment.services import run_etl_service


url = f"sqlite:///{str(Path.home().joinpath('.sfl_assignment', 'users.db'))}"

config = Configuration(
    environment='local',
    data_access={'base_path': None},
    database={'url': url}
)

run_etl_service(config, '../data/DATA.csv')

db=sqlalchemy.create_engine(url)
df = pd.read_sql('select * from users',db)
print(df)
