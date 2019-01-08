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

# KEYWORDS_LIST = os.environ.get('KEYWORDS_LIST', '').split(',')


class Index(tornado.web.RequestHandler):
    def get(self):
        langs = []
        tweets = []
        # for key in KEYWORDS_LIST:
        #     langs.append({
        #         "name": key,
        #         "count": db.get(key)
        #     })
        #     tweets.append({
        #         "user": db.get('tw:'+key+':img'),
        #         "tw": db.get('tw:'+key)
        #     })
        self.render('index.html',
                    langs=langs,
                    tweets=tweets)


class Status(tornado.web.RequestHandler):
    def get(self, tag):
        count = db.get(tag)
        self.write(json.dumps(count))


class Tweets(tornado.web.RequestHandler):
    def post(self):
        lang = self.get_argument('lang', 'python')
        self.write(json.dumps(db.get('tw:'+lang)))


if __name__ == '__main__':
	tornado.options.parse_command_line()
	app = tornado.web.Application(
		handlers=[(r'/', Index), (r'/tweets', Tweets), (r'/status/(.*)', Status)],
		template_path=os.path.join(os.path.dirname(__file__), "tpl"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
	)
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
