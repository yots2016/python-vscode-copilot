from PIL import Image, ImageDraw
import io
from http.server import SimpleHTTPRequestHandler

def image(handler: SimpleHTTPRequestHandler):
    img = Image.new('RGB', (300, 100), color=(73, 109, 137))
    d = ImageDraw.Draw(img)
    d.text((10, 40), "Hello from Pillow!", fill=(255, 255, 0))
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    img_bytes = buf.getvalue()
    handler.send_response(200)
    handler.send_header('Content-type', 'image/png')
    handler.send_header('Content-Length', str(len(img_bytes)))
    handler.end_headers()
    handler.wfile.write(img_bytes)
