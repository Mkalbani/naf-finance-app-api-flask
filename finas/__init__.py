import os
from flask import Flask, request, render_template, redirect, url_for, flash, session
from sqlalchemy import exc
from finas.db import *
from finas.cashier.routes import cashier
from finas.autho.routes import autho
from finas.clerk.routes import clerk
from finas.fo.routes import fo
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from dotenv import load_dotenv #load env


load_dotenv()

#initiate app

app = Flask(__name__)

app.secret_key = 'sdghsduhfiueyt834r9823sdjffow3iur93weudjs83wr'


app.config.from_object(os.environ.get('config'))

db.init_app(app)


login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "index"

@login_manager.user_loader
def load_user(user_id):
    return Admn.query.get(user_id)


from finas.api.routes import api
app.register_blueprint(api)
app.register_blueprint(cashier)
app.register_blueprint(autho)
app.register_blueprint(clerk)
app.register_blueprint(fo)


from finas.filters import *

@app.context_processor
def everywhere():
    session['title'] = 'UNIT FINANCIAL ACCOUTNING SOFTWARE'
    return dict()

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = Admn.query.filter_by(usern=username).first()
        if user:
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Invalid login credentials')
    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')