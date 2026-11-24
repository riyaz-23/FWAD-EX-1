"""A tiny web server that serves the files in this folder.

Run it with:   python server.py
Then open:     http://localhost:8000
Stop it with:  Ctrl + C
"""

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

HOST = "127.0.0.1"   # localhost: only this computer can connect
PORT = 8000          # the "door number" the server listens on


class MyHandler(SimpleHTTPRequestHandler):
    """Handles each browser request. Serves index.html for '/'."""

    def log_message(self, format, *args):
        # Print a short line for every request so you can watch the traffic
        print(f"Request from {self.client_address[0]}: {self.path}")


if __name__ == "__main__":
    server = ThreadingHTTPServer((HOST, PORT), MyHandler)
    print(f"Server running at http://localhost:{PORT}  (Ctrl + C to stop)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        server.server_close()
