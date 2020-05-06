from main import app
from flask import request
from src.db import API

db = API()


@app.route('/get_data', methods=["GET"])
def get_data():
    key = request.args.get("key")
    return db.read_data(key)


@app.route('/write_data', methods=["PUT"])
def upsert_data():
    resp = db.write_data(request.json['key'], request.json['data'])
    if resp is None:
        return {}
    return resp
