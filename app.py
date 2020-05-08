from flask import Flask
from src import requests, views
from config import config

app = Flask(__name__)

if __name__ == '__main__':
    app.register_blueprint(requests)
    app.register_blueprint(views)
    app.run(config.server.host, config.server.port)
