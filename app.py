from flask import Flask
from src.handlers import requests, views
from config import config

app = Flask(__name__)

if __name__ == '__main__':
    for blueprint in [requests, views]:
        app.register_blueprint(blueprint)
    app.run(config.server.host, config.server.port)
