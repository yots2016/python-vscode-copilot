import pyautogui

def f14(handler):
    pyautogui.press('f14')
    handler.send_response(200)
    handler.send_header('Content-type', 'text/plain')
    handler.end_headers()
    handler.wfile.write(b'F14 pressed')
