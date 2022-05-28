from flask import Blueprint, render_template

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/analysis/')
def main_analysis():
    return render_template('analysis/index.html')