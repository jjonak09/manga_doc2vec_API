from alchemydb import Base, engine


class Manga(Base):
    __tablename__ = "manga_info"
    __table_args__ = {"autoload": True}
