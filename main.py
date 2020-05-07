# from config.config import parse_config
# from constants import CONFIG_DIR_PATH
from flask import Flask
app = Flask(__name__)
from src import requests, views
