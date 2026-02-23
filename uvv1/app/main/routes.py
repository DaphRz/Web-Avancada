from flask import current_app   # so chama a instancia q esta rodando - e nao o app q ja esta rodando (reler toda a aplicacçõa)
from app.main import main       # Dá certo pq a Aplicação é Modularizada

@main.route('/')   # decorator tomando conta das rotas
@main.route('/index')  # criando end point

def index():
    ambiente = current_app.config.get('ENV', "desconhecido")   # ambiente = current_app.config.get('CONFIG_NAME', "desconhecido")
    return f'Ola Mundo. Ambiente atual: {ambiente}'