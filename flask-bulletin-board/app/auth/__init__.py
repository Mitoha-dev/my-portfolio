from flask import Blueprint

# Blueprint を生成
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# routes.py を import してルートを登録
from . import routes