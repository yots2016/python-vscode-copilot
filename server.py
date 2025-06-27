import http.server
import socketserver
import os

PORT = 8000
DOCS_DIR = "swagger_ui_static"
SWAGGER_JSON_PATH = "swagger.json"
DOCS_PATH_PREFIX = "/api/docs/"

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == SWAGGER_JSON_PATH or self.path == "/" + SWAGGER_JSON_PATH:
            # Serve swagger.json from the root directory
            try:
                with open(SWAGGER_JSON_PATH, 'rb') as f:
                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(f.read())
                    return
            except FileNotFoundError:
                self.send_error(404, "File not found: swagger.json")
                return
        elif self.path.startswith(DOCS_PATH_PREFIX):
            # Serve files from DOCS_DIR, adjusting path
            # /api/docs/ -> /index.html
            # /api/docs/some.css -> /some.css
            relative_path = self.path[len(DOCS_PATH_PREFIX):]
            if not relative_path or relative_path.endswith('/'):
                relative_path += "index.html" # Serve index.html for /api/docs/ or /api/docs

            # Construct the full path to the file within DOCS_DIR
            file_path = os.path.join(DOCS_DIR, relative_path)

            # Security: Ensure the path is still within DOCS_DIR
            if not os.path.abspath(file_path).startswith(os.path.abspath(DOCS_DIR)):
                self.send_error(403, "Forbidden")
                return

            # Change directory to serve files relative to DOCS_DIR for SimpleHTTPRequestHandler
            # This is a bit of a workaround for SimpleHTTPRequestHandler's behavior
            original_cwd = os.getcwd()
            try:
                os.chdir(DOCS_DIR)
                # Update self.path to be relative to the new CWD (DOCS_DIR)
                self.path = "/" + relative_path
                super().do_GET()
            finally:
                os.chdir(original_cwd) # Restore CWD
            return
        elif self.path == "/":
             self.send_response(200)
             self.send_header("Content-type", "text/html")
             self.end_headers()
             self.wfile.write(b"<html><head><title>Test Server</title></head>")
             self.wfile.write(b"<body><h1>Server is running</h1>")
             self.wfile.write(b"<p>Swagger UI is available at <a href='/api/docs/'>/api/docs/</a>.</p>")
             self.wfile.write(b"</body></html>")
             return

        # For any other path, let SimpleHTTPRequestHandler try to serve it from the root
        # This might be useful for other static files if needed, but primarily for swagger.json
        super().do_GET()


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    print(f"Swagger UI available at http://localhost:{PORT}{DOCS_PATH_PREFIX}")
    print(f"Swagger JSON available at http://localhost:{PORT}/{SWAGGER_JSON_PATH}")
    httpd.serve_forever()
