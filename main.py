import urllib2
import logging
import time
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

logger = logging.getLogger('ArthurSay')

hdlr = logging.FileHandler('/var/tmp/arthur123.log')

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)

logger.addHandler(hdlr) 

logger.setLevel(logging.DEBUG)

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
        	logger.debug("request income")
        	return

try:

    # while True:
        # logger.debug(urllib2.urlopen("http://52.40.99.69:3000/").read())
        # time.sleep(3)

	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()


