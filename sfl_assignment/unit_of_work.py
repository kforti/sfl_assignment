from typing import Dict


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine



class SessionFactory:
    def __init__(self, config: Dict):
        self.config = config

    def __call__(self):
        engine = create_engine(self.config.get('url'))
        session = sessionmaker(bind=engine)
        return session()


class SQLAlchemyUnitofWork:
    def __init__(self, repository_cls, session_factory):
        self.session_factory = session_factory
        self.repository_cls = repository_cls

    def __enter__(self):
        self.session = self.session_factory()
        self.repository = self.repository_cls(self.session)
        return self

    def __exit__(self, *args):
        self.rollback()
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        # self.session.rollback()
        return