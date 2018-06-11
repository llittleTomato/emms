from . import view
from flask import render_template


@view.route('/')
def index():
    data = 'hello world---'
    return render_template('index.html', data=data)
