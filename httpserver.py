from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		# Send the html message
		self.wfile.write("Hello Arthur !")
		return

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()


### 1
# import sys
# import BaseHTTPServer
# from SimpleHTTPServer import SimpleHTTPRequestHandler

# HandlerClass = SimpleHTTPRequestHandler
# ServerClass  = BaseHTTPServer.HTTPServer
# Protocol     = "HTTP/1.0"

# if sys.argv[1:]:
#   port = int(sys.argv[1])
# else:
#   port = 8000
# server_address = ('127.0.0.1', port)

# HandlerClass.protocol_version = Protocol
# httpd = ServerClass(server_address, HandlerClass)

# sa = httpd.socket.getsockname()
# print "Serving HTTP on", sa[0], "port", sa[1], "..."
# httpd.serve_forever()

### 2
# import SimpleHTTPServer
# import SocketServer

# PORT = 8000

# Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

# httpd = SocketServer.TCPServer(("0.0.0.0", PORT), Handler)

# print "serving at port", PORT
# httpd.serve_forever()