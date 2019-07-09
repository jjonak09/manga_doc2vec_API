# from gensim.models.doc2vec import Doc2Vec, TaggedDocument

# with open('text/title.txt', mode='r', encoding='utf-8') as f:
#     manga_title = f.read()
# manga_title = manga_title.split('\n')

# manga_index = {}
# for i, title in enumerate(manga_title):
#     manga_index[''.join(title)] = i

# model = Doc2Vec.load('model/manga_title.model')

# for p in model.docvecs.most_similar(manga_index['イナズマイレブン']):
#     print(manga_title[p[0]])


from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from alchemydb import Session, engine
from models import Manga
import urllib.parse


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
                "imaga_url": m.image_url
            })
    except Exception as e:
        print(e)
    finally:
        session.close()
        return result
