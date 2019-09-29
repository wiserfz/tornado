import tornado.web
import tornado.ioloop
import tornado.options
from tornado.httpserver import HTTPServer

# type 可以为 str,float,int,datetime,timedelta 如果没有设置type会根据default的值进行转换，如果也没有设置default则不会转换
# tornado.options.define("port", default=8000, type=int, help="端口", multiple=False)
# tornado.options.define("list", default=[], type=str, multiple=True)

from demo import configs


# view函数
class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("Hello, tornado!")


if __name__ == "__main__":
    # 解析命令行参数,并保存到options中
    # tornado.options.parse_command_line()
    # 解析配置文件，导入参数 path 相对于工程的目录
    # tornado.options.options.logging = None  # 关闭日志输出
    # tornado.options.parse_config_file(path="config")
    # print("list: {}".format(tornado.options.options.list))
    app = tornado.web.Application([
        # 路由
        (r"/", IndexHandler)
    ])
    # 创建默认 httpserver
    # app.listen(8000)
    # 实例化一个 httpserver
    http_server = HTTPServer(app)
    # 绑定端口 默认单进程
    # http_server.listen(tornado.options.options.port)  # tornado.options.options是全局变量，上面定义的属性都通过它去使用
    http_server.listen(configs.options.port)
    # 服务器绑定端口
    # http_server.bind(8000)
    # 启动2个进程
    # http_server.start(1)

    tornado.ioloop.IOLoop.current().start()
