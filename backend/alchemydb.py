from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging

RDB_PATH = 'sqlite:///manga.db'
ECHO_LOG = False
engine = create_engine(
    RDB_PATH, echo=ECHO_LOG
)
Base = declarative_base(engine)
Session = sessionmaker(bind=engine)
