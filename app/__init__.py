from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Routes register
    from app.routes import register_routes
    register_routes(app)
    
    return app

app = create_app()