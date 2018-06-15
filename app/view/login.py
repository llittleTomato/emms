from . import view
from flask import render_template, url_for
from app.forms.login.login import LoginForm


@view.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login_test.html', title="Sign In", form=form)
