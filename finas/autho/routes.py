from flask import Blueprint

autho = Blueprint('autho', __name__, url_prefix='/autho')

@autho.route('/home')
def home():
    return "this is home from Authorising Officer"