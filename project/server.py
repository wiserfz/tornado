import tornado.ioloop

import project.configs as configs
from project.application import Application

if __name__ == "__main__":
    app = Application()
    app.listen(configs.options["port"])
    tornado.ioloop.IOLoop.current().start()
