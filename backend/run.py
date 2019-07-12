import responder
import urllib.parse
import traceback
import json
from setting import Session
from models import Manga
from get_manga_info import get_manga_list, get_manga
from manga_doc2vec import result_doc2vec

api = responder.API(cors=True, cors_params={
    'allow_origins': ['*']
})

# idに合ったmangaデータをjsonで返す


@api.route("/api/manga/{id}")
def users_json(req, resp, *, id):
    session = Session()
    try:
        manga = session.query(Manga).filter_by(id=id).first()
        if manga:
            resp.headers = {"Content-Type": "application/json; charset=utf-8"}
            resp.content = json.dumps(
                get_manga(manga), indent=2, ensure_ascii=False)
    except Exception:
        traceback.print_exc()
        resp.media = {"errmessage": "Error occured"}
    finally:
        session.close()


# mangaのlistを全て返す

@api.route("/api/mangas")
def users_json(req, resp):
    session = Session()
    try:
        mangas = session.query(Manga).all()
        resp.headers = {"Content-Type": "application/json; charset=utf-8"}
        resp.content = json.dumps(
            get_manga_list(mangas), indent=2, ensure_ascii=False)

    except Exception:
        traceback.print_exc()
        resp.media = {"errmessage": "Error occured"}
    finally:
        session.close()

# doc2vec 類似している漫画を探す


@api.route("/api/title/{title}")
def users_json(req, resp, *, title):
    # urlのデコード
    title = urllib.parse.unquote(title)

    resp.headers = {"Content-Type": "application/json; charset=utf-8"}
    resp.content = result_doc2vec(title)


if __name__ == '__main__':
    api.run()
