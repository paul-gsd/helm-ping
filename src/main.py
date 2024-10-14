import http.server
import socketserver

PORT = 8080

class PingPongHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path != '/api/ping':
            self.send_response(404)
            self.end_headers()
            return
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'pong')

with socketserver.TCPServer(("", PORT), PingPongHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
