from . import view
from flask import render_template, url_for


@view.route('/', methods=['GET', 'POST'])
def login():

    data = 'aaa'
    return render_template('login.html', data=data)
