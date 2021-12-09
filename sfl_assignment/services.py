from pathlib import Path

from .models import Configuration, UserRepository
from .data_access import local_csv_data_access_factory, s3_csv_data_access_factory
from .pipeline import run_etl_pipeline
from .unit_of_work import SQLAlchemyUnitofWork, SessionFactory



DATA_ACCESS_FACTORIES = {
    ('local', 'csv'): local_csv_data_access_factory,
    ('aws', 'csv'): s3_csv_data_access_factory
}


def run_etl_service(config: Configuration, file_name):
    file_type = file_name.split('.')[-1]
    data_access_factory = DATA_ACCESS_FACTORIES[(config.environment, file_type)]
    data_access = data_access_factory(config.data_access)

    unit_of_work = SQLAlchemyUnitofWork(repository_cls=UserRepository,
                                        session_factory=SessionFactory(config.database))
    run_etl_pipeline(file_name=file_name,
                     data_access=data_access,
                     unit_of_work=unit_of_work)
