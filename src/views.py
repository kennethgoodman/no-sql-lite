from flask import render_template, Blueprint
views = Blueprint('views', __name__, template_folder='templates')

@views.route('/')
def home():
    return "<b>Welcome To NoSQL-Lite!</b>"


@views.route('/get_data_page')
def template():
    return render_template('get_data_page.html')
