import os

from tornado import web

from project.configs import settings, BASE_DIR
from project import views


class Application(web.Application):

    def __init__(self):
        handlers = [
            #(r"/", views.index.IndexHandle),
            # 反向解析
            web.url(r"/home/", views.index.HomeHandle, name="home"),
            # 路径传参
            # (r"/parms/(\w+)/(\d+)/", views.index.ParmsIndex),
            (r"/parms/(?P<kind>\w+)/(?P<age>\d+)/", views.index.ParmsIndex),
            # get传参
            (r"/getparms/", views.index.GetParms),
            # post传参
            (r"/postparms/", views.index.PostParms),
            # request
            (r"/request/", views.index.RequestTest),
            # upload
            (r"/uploadfile/", views.index.UploadHandler),
            # login
            web.url(r"/login/", views.index.LoginHandler, name="login"),
            # staticFileHandler 必须放在所有路由下面
            (r"/(.*)$", views.index.StaticFileHandler, {"path": os.path.join(BASE_DIR, "static/html"),
                                                "default_filename": "index.html"})
        ]
        super().__init__(handlers, **settings)
