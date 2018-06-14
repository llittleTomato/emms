from flask import Blueprint


view = Blueprint('view', __name__)

from . import index
from app.view.login import login
