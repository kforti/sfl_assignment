from sfl_assignment.models import Configuration
from sfl_assignment.services import run_etl_service

import sqlalchemy
import pandas as pd

config = Configuration(
    environment='local',
    data_access={'base_path': None},
    database={'url': "sqlite:////home/kevin/bin/sfl_assignment/sfl_assignment/users.db"}
)

run_etl_service(config, '../data/DATA.csv')

db=sqlalchemy.create_engine('sqlite:////home/kevin/bin/sfl_assignment/sfl_assignment/users.db')
df = pd.read_sql('select * from users',db)
print(df)