import http.server
import socketserver
import os
from app.controller import MainController

PORT = 8000
DIRECTORY = os.path.join(os.path.dirname(__file__), '..', 'static')
controller = MainController()

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def send_static(self):
        return super().do_GET()

    def do_GET(self):
        if self.path == "/":
            return controller.hello(self)
        elif self.path == "/f14":
            return controller.f14(self)
        elif self.path == "/image":
            return controller.image(self)
        elif self.path == "/endpoints":
            return controller.list_endpoints(self)
        return super().do_GET()

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        httpd.serve_forever()
