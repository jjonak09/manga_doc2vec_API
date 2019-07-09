import responder
import traceback
import urllib.parse
import json
from alchemydb import Session, engine
from models import Manga

from sqlutils import alchemytojson, alchemytodict
from manga_title import result_doc2vec

api = responder.API()


@api.route("/api/manga/{id}")
def users_json(req, resp, *, id):
    session = Session()
    try:
        manga = session.query(Manga).filter_by(id=id).first()
        resp.headers = {"Content-Type": "application/json; charset=utf-8"}
        resp.content = alchemytojson(manga)
    except Exception:
        traceback.print_exc()
        resp.media = {"errmessage": "Error occured"}
    finally:
        session.close()
        print(engine.pool.status())


@api.route("/api/title/{title}")
def users_json(req, resp, *, title):
    # urlのデコード
    title = urllib.parse.unquote(title)

    resp.headers = {"Content-Type": "application/json; charset=utf-8"}
    resp.content = json.dumps(result_doc2vec(
        title), indent=2, ensure_ascii=False)


@api.route("/api/mangas")
def users_json(req, resp):
    session = Session()
    try:
        mangas = session.query(Manga).all()
        resp.headers = {"Content-Type": "application/json; charset=utf-8"}
        resp.content = alchemytojson(mangas)
    except Exception:
        traceback.print_exc()
        resp.media = {"errmessage": "Error occured"}
    finally:
        session.close()
        print(engine.pool.status())


if __name__ == '__main__':
    api.run()
