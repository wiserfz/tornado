import os

from tornado.web import RequestHandler, StaticFileHandler, authenticated

from project import configs


class IndexHandle(RequestHandler):

    # 设置响应头
    def set_default_headers(self):
        print("set_default")

    # 参数初始化
    def initialize(self):
        print("initialize")

    # 预处理，反爬虫等
    def prepare(self):
        print("prepare")

    # http方法
    def get(self):
        print("http方法")
        url = self.reverse_url("home")
        self.write("Hello tornado!\n <a href='%s'>jump</a>" % url)

    # 返回错误
    def write_error(self, status_code: int, **kwargs):
        print("write_error")

    # 请求结束后的处理，日志处理等
    def on_finish(self):
        print("on_finish")


class LoginHandler(RequestHandler):

    def get(self):
        page = self.get_query_argument("next", "/")
        url = "/login/?next=" + page
        self.render("login.html", url=url)

    def post(self):
        user = self.get_body_argument("username")
        pwd = self.get_body_argument("password")
        page = self.get_query_argument("next", "/")
        if user == "Jacob" and pwd == "123456":
            self.redirect(page + "?flag=logined")
        else:
            url_name = self.reverse_url("login")
            self.redirect(url_name + "?next=" + page)


class HomeHandle(RequestHandler):

    def get_current_user(self):
        flag = self.get_query_argument("flag", None)
        if flag:
            return True
        else:
            return False

    @authenticated
    def get(self):
        self.render("home.html")


class ParmsIndex(RequestHandler):

    # http方法
    def get(self, age, kind):
        self.write("Jacob is %s, age is %d" % (kind, int(age)))


class GetParms(RequestHandler):

    def get(self):
        name = self.get_query_argument("name")
        kind = self.get_query_argument("kind")
        age = int(self.get_query_argument("age", default=18))
        self.write("%s is %s, age is %d" % (name, kind, age))


class PostParms(RequestHandler):
    # 渲染界面
    def get(self):
        self.render('xxx.html')

    def post(self):
        username = self.get_body_argument("username")
        pwd = self.get_body_argument("password")
        hobby = self.get_body_arguments("hobby")
        print(username, pwd, hobby)
        # 即获取get参数也获取post参数 最好不要选用
        # args1 = self.get_argument() / self.get_arguments()
        self.write("login success!")


class RequestTest(RequestHandler):

    def get(self):
        print(self.request.remote_ip)


class UploadHandler(RequestHandler):

    def get(self):
        self.set_cookie("name", "val",)
        self.render("upload.html")

    def post(self):
        # 上传文件的对象
        files = self.request.files
        for file in files:
            file_list = files.get(file)
            for file_obj in file_list:
                # 存储路径
                file_path = os.path.join(configs.BASE_DIR, "upload", file_obj.filename)
                with open(file_path, "wb") as f:
                    # 将文件打碎，一块一块写
                    for part in f.chunks():
                        f.write(part)
                        f.flush()
        self.write("ok")


class StaticFileHandler(StaticFileHandler):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.xsrf_token
