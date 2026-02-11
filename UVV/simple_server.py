# Criando uma pág HTML dentro do Python

from http.server import HTTPServer, BaseHTTPRequestHandler


class MyHandler(BaseHTTPRequestHandler):                 # MyHandler = meu manipulador # Criei class por herança explicita
    def do_GET(self):                                    # Criando Verbo (Get)
        self.send_response(200)                          # Responder por padrão Status 200 se tudo ocorrer bem
        self.send_header("Content-type", "text/html")
        self.end_headers()
        message = "<html><body><h1>Ola, mundo!</h1></body></html>"
        self.wfile.write(message.encode())               # Pega o de cima e transforma em

if __name__ == "__main__":           # Instrução do Python - executado em sequência - oq eu qro rodar e oq não
    server_addres = ('', 8000)       # Informando pro servidor o endereço em q ele vai rodar - '' = dominio (localhost), 8000 = porta - pra nao ir pra porta 80 (portas que ja estao rodando na maquina)
    htppd = HTTPServer(server_addres, MyHandler)   # Pegando o servidor web - ativando - vai pegar o meu endereço e o meu método (verbo get)
    print('Servidor rodando em http://localhost:8000')
    htppd.serve_forever()            # Quando acende servidor web, não desliga mais