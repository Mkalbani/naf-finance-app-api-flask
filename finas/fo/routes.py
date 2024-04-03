from flask import Blueprint

fo = Blueprint('fo', __name__, url_prefix='/fo')

@fo.route('/home')
def home():
    return "home from Fin Offr"