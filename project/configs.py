import os

BASE_DIR = os.path.dirname(__file__)

# 参数
options = {
    "port": 8000,
}

# db
mysql = {
    "host": "127.0.0.1",
    "user": "root",
    "passwd": "abcabc",
    "dbName": "",
}

# 配置
settings = {
    # 调试模式，上线后需要改为False，debug为True相当于设置以下4项设置
    "debug": True,
    # 只想启动自启服务
    #"autoreload": True,
    # 取消缓存编译模版
    #"compiled_template_cache": False,
    # 取消缓存静态文件的hash值
    #"static_hash_cache": False,
    # 提供报错追踪信息
    #"serve_traceback": True,
    "template_path": os.path.join(BASE_DIR, "template"),
    "static_path": os.path.join(BASE_DIR, "static"),
    # 关闭当前项目的自动转译功能，模版的转译功能
    #"autoescape": None,
    # 安全cookie的密钥 用某种规则生成对应值通过base64和uuid生成一串字符串
    "cookie_secret": "LCcYRomlTL6/h/xW9dumX6thHaL9zUjGk32d91mWXiY=",
    # xsrf保护
    "xsrf_cookies": True,
    "login_url": "/login/"
}
