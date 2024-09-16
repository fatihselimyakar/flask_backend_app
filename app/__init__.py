from flask import Flask
from .models import create_tables, close_connection
from .routes import bp as routes_bp
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)
    # Konfigürasyonları buraya ekleyin
    # app.config.from_object('config.Config')

    # Tabloları oluştur
    @app.before_request
    def initialize_tables():
        app.before_request_funcs[None].remove(initialize_tables)
        create_tables()
        

    # Yolları (routes) kaydet
    app.register_blueprint(routes_bp)

    app.teardown_appcontext(close_connection)

    return app
