import responder
import urllib.parse
from get_manga_info import get_manga_list, get_manga
from manga_doc2vec import result_doc2vec

api = responder.API()


@api.route("/api/manga/{id}")
def users_json(req, resp, *, id):
    resp.headers = {"Content-Type": "application/json; charset=utf-8"}
    resp.content = get_manga(id)


@api.route("/api/title/{title}")
def users_json(req, resp, *, title):
    # urlのデコード
    title = urllib.parse.unquote(title)

    resp.headers = {"Content-Type": "application/json; charset=utf-8"}
    resp.content = result_doc2vec(title)


@api.route("/api/mangas")
def users_json(req, resp):
    resp.headers = {"Content-Type": "application/json; charset=utf-8"}
    resp.content = get_manga_list()


if __name__ == '__main__':
    api.run()
