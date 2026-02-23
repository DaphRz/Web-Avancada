# from flask import Flask
# app = Flask(__name__)  # Criado sem factory -- nao recomendado

import os
from app import create_app

config_name = os.getenv('FLASK_CONFIG') or os.getenv('FLASK_ENV') or 'default'

app = create_app(config_name)

print(f'[DEBUG] app.debug = {app.debug}')
print(f'[DEBUG] config_name = {config_name}')

if __name__ == '__main__':
    app.run()