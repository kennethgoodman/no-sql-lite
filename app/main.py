from flask import Flask
from src import requests, views
from config import config

app = Flask(__name__)
for blueprint in [requests, views]:
    app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(config.server.host, config.server.port, debug=True)
