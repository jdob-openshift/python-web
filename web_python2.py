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

    server = HTTPServer(('', PORT_NUMBER), MyHandler)
    print('Serving at port:', PORT)
   
    server.serve_forever()


if __name__ == '__main__':
    run()
