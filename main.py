import socket
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        # Получаем внутренний IP адрес сервера
        ip_address = socket.gethostbyname(socket.gethostname())
        # Отправляем IP адрес в теле ответа
        self.wfile.write(ip_address.encode())

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8080):
    server_address = ('', port)
    with server_class(server_address, handler_class) as httpd:
        print(f'Starting httpd on port {port}')
        httpd.serve_forever()

if __name__ == "__main__":
    run()
