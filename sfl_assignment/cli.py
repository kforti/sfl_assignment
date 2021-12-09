from pathlib import Path
import shutil

import click
import sqlalchemy
import pandas as pd

from .build_database import sqlite_connection_factory, build_users_db
from .models import Configuration
from .services import run_etl_service


@click.command()
@click.option('--env', default='local', help='location of pipeline environment')
@click.argument('file_path')
def run_etl_pipeline(env, file_path):
    url = f"sqlite:///{str(Path.home().joinpath('.sfl_assignment', 'users.db'))}"
    config = Configuration(
        environment=env,
        data_access={'base_path': None},
        database={'url': url}
    )

    run_etl_service(config, file_path)


DATABASES = {
    'sqlite': sqlite_connection_factory
}


@click.command()
@click.argument('database')
def create_database(database):
    Path.home().joinpath('.sfl_assignment').mkdir()
    conn_factory = DATABASES[database]
    build_users_db(conn_factory)


@click.command()
@click.argument('database')
def remove_database(database):
    if database == 'sqlite':
        path = Path.home().joinpath('.sfl_assignment')
        shutil.rmtree(path)


@click.command()
def print_all_records():
    url = f"sqlite:///{str(Path.home().joinpath('.sfl_assignment', 'users.db'))}"
    db = sqlalchemy.create_engine(url)
    df = pd.read_sql('select * from users', db)
    for record in df.to_dict(orient='records'):
        print(record)