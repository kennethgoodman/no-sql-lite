from main import app
from flask import render_template


@app.route('/')
def home():
    return "<b>Welcome To NoSQL-Lite</b>"


@app.route('/get_data_page')
def template():
    return render_template('get_data_page.html')
