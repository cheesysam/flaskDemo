import SimpleHTTPServer, BaseHTTPServer
import random

PORT = 1234

class request_handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def number_generator(self):
        return random.randint(1,100)

    def do_GET(self):
	print 'get request'
	returnString = '{"data":{"cpu":['
        for i in range(10):
            returnString += str(self.number_generator())
	    returnString += ', ' if i is not 9 else ''
	returnString += '], "mem":['
        for i in range(10):
            returnString += str(self.number_generator())
	    returnString += ', ' if i is not 9 else ''
	returnString += ']}}'
        self.wfile.write(returnString)
	return

def start_server():
    """Start the server."""
    server_address = ("", PORT)
    server = BaseHTTPServer.HTTPServer(server_address, request_handler)
    server.serve_forever()

if __name__ == "__main__":
    start_server()
