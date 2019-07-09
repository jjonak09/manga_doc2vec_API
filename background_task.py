import responder
import time

api = responder.API()


@api.route("/")
def hello(req, resp):

    @api.background.task
    def sleep(s=10):
        time.sleep(s)
        print('sleeped!')
    sleep()
    resp.content = "processing!"


if __name__ == '__main__':
    api.run()


# import responder
# import time

# api = responder.API()


# @api.route("/incoming")
# async def receive_incoming(req, resp):

#     # バックグランドタスク
#     @api.background.task
#     def process_data(data):
#         time.sleep(3)

#     data = await req.media()

#     process_data(data)

#     resp.media = {'success': True}

# if __name__ == '__main__':
#     api.run()
