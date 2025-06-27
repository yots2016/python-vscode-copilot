def list_endpoints_html(handler):
    """Generates an HTML page listing all available endpoints."""
    endpoints = [
        {"path": "/", "description": "Displays a friendly hello message."},
        {"path": "/f14", "description": "Shows information about the F14 aircraft."},
        {"path": "/image", "description": "Displays an image."},
        {"path": "/endpoints", "description": "Lists all available endpoints (this page)."}
    ]

    html_content = "<html><head><title>Available Endpoints</title></head><body>"
    html_content += "<h1>Available Endpoints</h1><ul>"
    for endpoint in endpoints:
        html_content += f"<li><a href='{endpoint['path']}'>{endpoint['path']}</a>: {endpoint['description']}</li>"
    html_content += "</ul></body></html>"

    handler.send_response(200)
    handler.send_header("Content-type", "text/html")
    handler.end_headers()
    handler.wfile.write(html_content.encode('utf-8'))
    return handler
