import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import json
import redis


from tornado.options import define, options
define("port", default=5000, help="run on the given port", type=int)

db = redis.Redis(host='redis', port=6379, db=0)

class Index(tornado.web.RequestHandler):
    def get(self):
        data = []
        data_dict = db.hgetall('FULLVIEW')

        for key in data_dict.keys():
            data.append(json.loads(data_dict[key].decode("utf-8")))
        data = sorted(data, key=lambda d: d['capital'], reverse=True)
        self.render('index.html',hold=data)


class Full(tornado.web.RequestHandler):
    def get(self):
        data = []
        data_dict = db.hgetall('FULLVIEW')

        for key in data_dict.keys():
            data.append(json.loads(data_dict[key].decode("utf-8")))

        data = sorted(data, key=lambda d: d['capital'], reverse=True)
        self.write(json.dumps(data))


if __name__ == '__main__':
	tornado.options.parse_command_line()
	app = tornado.web.Application(
		handlers=[(r'/', Index), (r'/full', Full)],
		template_path=os.path.join(os.path.dirname(__file__), "tpl"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
	)
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
