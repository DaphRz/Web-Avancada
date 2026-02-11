# Deu errado o meu

from my_webserver import MyWebServer   # from = carregar biblioteca. (estou carregando meu arquivo)
from http.server import SimpleHTTPRequestHandler
import os  # acessar sistema operacional

PORT = int(os.getenv("PORT", 3001))    # Porta Padrão 3001

class ManuseiroHTTPRequest(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":           # / = rotas - endpoint (/ do endereço da página (google.com/daphne))
            self.send_response(200)
            self.send_header("Content-type", "text/html charset=utf-8")
            self.end_headers()
            self.wfile.write("<p>Ola, Mundo!</p>".encode())

        else:
            self.send_error(404)

app = MyWebServer(ManuseiroHTTPRequest)

if __name__ == "__main__":
    app.run()