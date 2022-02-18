from http.server import HTTPServer, BaseHTTPRequestHandler
import time

HOST = "127.0.0.1"
PORT = 9999

class NroubHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body>Hi,<br>Wailcome to our website<br>http://www.nroub.com/</body></html>", "utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "applicatipn/json")
        self.end_headers()

        date = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(time.time()))
        self.wfile.write(bytes('{"time" : "' + date + '"}', "utf-8"))

server = HTTPServer((HOST, PORT), NroubHTTP)
print("Server now running...")
server.serve_forever()
server.server_close()
print("Server now stopped!")
