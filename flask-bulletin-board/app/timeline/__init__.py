from flask import Blueprint

timeline_bp = Blueprint('timeline', __name__)

from . import routes