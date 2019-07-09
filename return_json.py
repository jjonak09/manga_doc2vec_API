import responder

api = responder.API()


@api.route("/hello/{who}/json")
def hello_to(req, resp, *, who):
    # mediaでjson返す
    resp.media = {"hello": who}


if __name__ == '__main__':
    api.run()
