import unittest
import threading
import time
import requests
import os
import sys
import signal

from http.server import HTTPServer
from app import server

class ServerThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.daemon = True
        self.httpd = None

    def run(self):
        os.chdir(os.path.dirname(os.path.dirname(__file__)))
        self.httpd = server.socketserver.TCPServer(("", server.PORT), server.Handler)
        self.httpd.serve_forever()

    def stop(self):
        if self.httpd:
            self.httpd.shutdown()
            self.httpd.server_close()

class IntegrationTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server_thread = ServerThread()
        cls.server_thread.start()
        time.sleep(1)  # Give server time to start

    @classmethod
    def tearDownClass(cls):
        cls.server_thread.stop()
        time.sleep(1)

    def test_hello_html(self):
        resp = requests.get(f"http://localhost:{server.PORT}/")
        self.assertEqual(resp.status_code, 200)
        self.assertIn("Hello, world!", resp.text)

    def test_f14_endpoint(self):
        resp = requests.get(f"http://localhost:{server.PORT}/f14")
        self.assertEqual(resp.status_code, 200)
        self.assertIn("F14 pressed", resp.text)

if __name__ == "__main__":
    unittest.main()
