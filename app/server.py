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
        elif self.path == "/openapi.json":
            # Serve the openapi.json file from the static directory
            self.path = "/openapi.json" # self.path is already correct
            return super().do_GET()
        elif self.path.startswith("/swagger/"):
            if self.path == "/swagger/" or self.path == "/swagger/index.html":
                # Serve swaggerui/index.html for /swagger/ or /swagger/index.html
                self.path = "/swaggerui/index.html"
            else:
                # Serve other swaggerui static files by prefixing with swaggerui
                # e.g. /swagger/swagger-ui.css -> /swaggerui/swagger-ui.css
                self.path = "/swaggerui/" + self.path[len("/swagger/"):]
            return super().do_GET()

        # For any other path, try to serve from static directory (default behavior)
        # This handles general static files like hello.html if not handled by specific endpoints
        return super().do_GET()

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        print(f"Swagger UI available at http://localhost:{PORT}/swagger/")
        httpd.serve_forever()
