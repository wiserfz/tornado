from tornado.web import RequestHandler

from .tornadoSQL import TornadoSQL


class ORM(RequestHandler):

    def save(self):
        pass