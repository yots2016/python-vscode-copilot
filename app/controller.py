from app.endpoints.hello import hello_html
from app.endpoints.f14 import f14
from app.endpoints.image import image

class MainController:
    def hello(self, handler):
        return hello_html(handler)

    def f14(self, handler):
        return f14(handler)

    def image(self, handler):
        return image(handler)
