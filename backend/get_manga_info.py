import copy
import json
from setting import Session
from models import Manga

# idに合ったmangaデータをjsonで返す


def get_manga(id):
    manga_dict = {}
    try:
        session = Session()
        manga = session.query(Manga).filter_by(id=id).first()
        if manga:
            manga_dict = {
                "id": manga.id,
                "title": manga.title,
                "manga_url": manga.manga_url,
                "imaga_url": manga.image_url,
                "tag": manga.tag
            }
    except Exception as e:
        print(e)
    finally:
        session.close()
        return json.dumps(manga_dict, indent=2, ensure_ascii=False)

# mangaのlistを全て返す


def get_manga_list():
    manga_list = []
    try:
        session = Session()
        mangas = session.query(Manga).all()
        for manga in mangas:
            manga_list.append({
                "id": manga.id,
                "title": manga.title,
                "manga_url": manga.manga_url,
                "imaga_url": manga.image_url,
                "tag": manga.tag
            })
    except Exception as e:
        print(e)
    finally:
        session.close()
        return json.dumps(manga_list, indent=2, ensure_ascii=False)
