from flask import Blueprint

view = Blueprint('view', __name__)

from . import index
from . import login
