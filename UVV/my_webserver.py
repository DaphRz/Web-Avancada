import http.server as http_server

class MyWebServer:   # Criando Objeto
    def __init__(self, http_hander=http_server.SimpleHTTPRequestHandler) -> None:  # init = inicializar (metodo de inicialização)
        self.http_hander = http_server

    def run(self, host="localhost", port=3001):
        httpd = http_server.HTTPServer((host, port), self.http_hander)
        print(f"Servidor rodando em {host}:{port}")
        httpd.serve_forever()   