from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# DB path
RDB_PATH = 'sqlite:///manga.db'

# engine: DBへの接続を表すオブジェクト
# create_engineでDBで接続
engine = create_engine(
    RDB_PATH, echo=False
)

# 各modelで利用
# classとDBをMapping
# declarativeを使用すると、クラス定義が自動的にテーブル定義とひもづく
Base = declarative_base(engine)

# DBに対してORM操作するときに利用
# Sessionを通じて操作を行う
Session = sessionmaker(bind=engine)
