def hello_html(handler):
    handler.path = "/hello.html"
    return handler.send_static()
