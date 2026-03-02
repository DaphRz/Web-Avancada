# Esse cód não é pra rodar - é um Passo a Passo

from flask import Flask
from sqlalchemy import db

app = Flask(__name__)   # criando objeto q é registrado (na memoria (?))

## Etapas Críticas da Aplicação (abaixo) 

# ! Fase de Configuração ! - construindo meu software - como funciona

# Declarar variáveis que vou usar / chaves de valor - vai ser colocada na memória
app.config['FOO'] = 'bar'
app.config['NAME_APP'] = 'delivery'

# Exemplo - Dic - Dicionário q eu vou criar
my_dic = {'KEY_1':  45, 'KEY_2': "Delivery", 'KEY_3': [34,'casa',[1,2]]}

# Registro de Rotas - endpoints
app.route('/')
app.add_url_rule('/',...)

# Registro do Blueprint
app.register_blueprint('name_blueprint')

# End Point - terminar
@main.route('/')
def

# Registro dos Métodos de Autenticação - (Biblioteca - admin)
admin = Admin(app)
admin.init_app(app)

db.init_app(app)

# Registro de Hooks (interceptar uma requisição / conexão - n deixar um usuario acessar admin (ex.))
@app.before_request
def before():
    pass

@app.errorhandler(404)
def not_found(error):
    return 'Não encontrado', 404

# Registro de Factory Secundária - outras views
views.init_app(app)
extension.init_app(app)

# ! Contexto de Aplicação ! - oq ela vai resolver / aplicar - manipulamos aplicação - no contexto de objeto / memoria - personalizo como funciona
current_app   # acessar app sem repetir / referenciar ela dnv
g             # variáveis globais podem dar problema

# Criando Extensão
from flask import current_app   # ir no obj da aplicação e devolver ...

def exemplo():
    valor = current_app.config('FOO')
    return valor

# ! Contexto de Request ! - Requisição à algum Servidor - pega um ambiente já pronto -

# Cabeçalhos HTTP 

## Parâmetro URL - ex. identificaçao usuario, "porta dos fundos"
# Porta dos Fundos
from flask import request

@app.route('/')
def hello():
    name = request.args.get("nome")
    return f'Ola {nome}'

# Validar Dados de Formulário - evitar ataque de injecao de dados

# Sessões (db, cliente) - gravação em cache (cliente)

# Objeto Request - criar regras request