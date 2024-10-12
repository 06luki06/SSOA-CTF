from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

class RequestLoggerHandler(BaseHTTPRequestHandler):
    def _send_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, this is a logging server!')

    def do_GET(self):
        self.log_request()
        self._send_response()

    def do_POST(self):
        self.log_request()
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        logging.info(f"POST data: {post_data.decode('utf-8')}")
        self._send_response()

    def log_request(self):
        logging.info(f"Incoming request: {self.command} {self.path}")
        for key, value in self.headers.items():
            logging.info(f"Header: {key} = {value}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
    server_address = ('', 8080)  # Listen on port 8080
    httpd = HTTPServer(server_address, RequestLoggerHandler)
    logging.info('Starting server on port 8080...')
    httpd.serve_forever()