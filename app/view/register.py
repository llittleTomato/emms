__author__ = 'sky'

from app.models import User, db
from . import view
from flask import render_template, url_for, request, redirect, flash
from app.forms.login.register import Register


@view.route('/register/', methods=['GET', 'POST'])
def register():
    form = Register(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('view.index'))
    else:
        return render_template('register.html')
