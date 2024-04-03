from flask import Blueprint

cashier = Blueprint('cashier', __name__, url_prefix='/cashier')

@cashier.route('/home')
def home():
    return "Welcome Home, Chill!"