from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import datetime

# tableの作成
engine = create_engine("sqlite:///manga.db")
base = automap_base()

base.prepare(engine, reflect=True)

table = base.classes.manga_info

# sessionの作成

session = sessionmaker(bind=engine)()
