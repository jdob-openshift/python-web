from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 8080

class MyHandler(BaseHTTPRequestHandler):
    
    #Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write("Hello World !")
        return

def run():

    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), MyHandler)
    print('Started httpserver on port %s' % PORT_NUMBER)
    
    #Wait forever for incoming htto requests
    server.serve_forever()

if __name__ == '__main__':
    run()
