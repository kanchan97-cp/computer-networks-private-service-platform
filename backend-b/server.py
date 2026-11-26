from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = "Hello from Backend B - Mac 4"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("X-Backend","B")
        self.end_headers()
        self.wfile.write(message.encode())

server = HTTPServer(("0.0.0.0", 3002), Handler)

print("Backend B running on port 3002...")
server.serve_forever()
