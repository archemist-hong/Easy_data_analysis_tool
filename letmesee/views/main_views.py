"""
file : letmesee/views/main_views.py
"""
from flask import Blueprint, render_template

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/')
def index():
    return render_template('index.html')

@main.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@main.route('/analysis/')
def index_analysis():
    return render_template('analysis/index.html')