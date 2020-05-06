from main import app
from flask import render_template


@app.route('/')
def home():
    return "<b>There has been a changes3</b>"


@app.route('/template')
def template():
    return render_template('src/templates/home.html')
