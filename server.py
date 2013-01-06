import SimpleHTTPServer, BaseHTTPServer
import random
import json

PORT = 1234

class request_handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def number_generator(self):
        return random.randint(1,100)

    def do_GET(self):
	print 'get request'
	generatedData = {"data":{"cpu":"", "mem":""}}
	generatedData["data"]["cpu"] = [self.number_generator() for x in range(10)]
	generatedData["data"]["mem"] = [self.number_generator() for x in range(10)]
	print generatedData
        self.wfile.write(json.dumps(generatedData))
	return

def start_server():
    """Start the server."""
    server_address = ("", PORT)
    server = BaseHTTPServer.HTTPServer(server_address, request_handler)
    server.serve_forever()

if __name__ == "__main__":
    start_server()
