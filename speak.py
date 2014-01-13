#!/bin/python
# coding: utf-8

import tornado.ioloop
import tornado.web
import mosquitto
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><body>'
                   '<form action="/" method="post">'
                   '<input type="text" name="message">'
                   '<input type="submit" value="はなす">'
                   '</form></body></html>')

    def post(self):
        self.write('<html><body>'
                   '<form action="/" method="post">'
                   '<input type="text" name="message">'
                   '<input type="submit" value="はなす">'
                   '</form></body></html>')


        payload = str(self.get_argument("message"))

        self.write(u"しゃべった言葉は " + payload)
        client = mosquitto.Mosquitto("test-client")
        client.connect("hostname")
        client.publish("topic", payload, 1)
        client.disconnect()


if __name__ == "__main__":

    client = mosquitto.Mosquitto("test-client")
    client.connect("hostname")

    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    application.listen(80)
    tornado.ioloop.IOLoop.instance().start()
