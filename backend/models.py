from setting import Base

# __table_args__ = {"autoload": True} で 既存のDBにアクセス


class Manga(Base):
    """
    MangaModel
    """
    __tablename__ = "manga_info"
    __table_args__ = {"autoload": True}
