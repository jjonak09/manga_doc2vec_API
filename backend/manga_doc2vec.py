from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from setting import Session
from models import Manga
import json


def result_doc2vec(title):
    result = []
    try:
        session = Session()
        manga = session.query(Manga).filter_by(title=title).first()
        model = Doc2Vec.load('model/manga_title.model')

        for p in model.docvecs.most_similar(manga.id - 1):
            m = session.query(Manga).filter_by(id=int(p[0])).first()
            result.append({
                "id": m.id,
                "title": m.title,
                "manga_url": m.manga_url,
                "imaga_url": m.image_url,
                "tag": m.tag
            })
    except Exception as e:
        print(e)
    finally:
        session.close()
        return json.dumps(result, indent=2, ensure_ascii=False)
