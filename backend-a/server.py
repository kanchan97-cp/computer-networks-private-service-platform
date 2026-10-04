from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = "Hello from Backend A - Mac 3"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("X-backend","A")
        self.end_headers()
        self.wfile.write(message.encode())

server = HTTPServer(("0.0.0.0", 3001), Handler)

print("Backend A running on port 3001...")
server.serve_forever()

