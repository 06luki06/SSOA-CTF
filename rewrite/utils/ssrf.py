from http.server import HTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Print request method and path
        print(f"Received GET request on path: {self.path}")
        # Print all incoming headers
        print("Headers:")
        for header, value in self.headers.items():
            print(f"{header}: {value}")
        # Send response
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'GET request received')

    def do_POST(self):
        # Print request method and path
        print(f"Received POST request on path: {self.path}")
        # Print all incoming headers
        print("Headers:")
        for header, value in self.headers.items():
            print(f"{header}: {value}")
        # Read and print the body
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        print("Body:")
        print(body.decode())
        # Send response
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'POST request received')

# Set up and start the server
def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}. Press Ctrl+C to stop.')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
