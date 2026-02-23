from flask import Flask

def create_app(config_name = 'development'):  # Criando a Infraestrutura -- foi criado por Factory  # Informando q estamos num amiente de desenvolvimento (development)
    app = Flask(__name__)  # Name é o app

    app.config.from_object('config.DevelopmentConfig')

    app.debug = app.config.get('DEBUG', False)

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app