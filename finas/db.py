from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash as gph, check_password_hash as cph

#intiate db
db = SQLAlchemy()

#db models

class Acct (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nam = db.Column(db.String, unique = True)
    descrip = db.Column(db.String)
    unitid = db.Column(db.Integer, db.ForeignKey('units.id'))
    trans = db.relationship('Trans', backref = 'acct_of_trans', lazy = 'dynamic')

class Admn(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    persid = db.Column(db.Integer, db.ForeignKey('pers.id'))
    usern = db.Column(db.String, unique = True)
    passw = db.Column(db.String)
    level = db.Column(db.Integer)
    trans = db.relationship('Trans', backref = 'admn_of_trans', lazy = 'dynamic')
    def is_valid(self, password):
        return cph(self.passw, password)
    def set_password(self, password):
        self.passw = gph(password)

class Comds (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nam = db.Column(db.String, unique = True)
    locid = db.Column(db.Integer, db.ForeignKey('locs.id'))
    order = db.Column(db.String)
    units = db.relationship('Units', backref = 'comd_of_unit', lazy = 'dynamic')

class Locs (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    locnam = db.Column(db.String, unique = True)
    units = db.relationship('Units', backref = 'loc_of_unit', lazy = 'dynamic')
    comds = db.relationship('Comds', backref = 'loc_of_Comd', lazy = 'dynamic')

class Pers (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    svcn = db.Column(db.String, unique = True)
    snam = db.Column(db.String)
    fnam = db.Column(db.String)
    onam = db.Column(db.String)
    rankid = db.Column(db.Integer, db.ForeignKey('ranks.id'))
    admn = db.relationship('Admn', backref = 'name_of_admn', lazy = 'dynamic')
    trans = db.relationship('Trans', backref = 'beneficiary_of_trans', lazy = 'dynamic')

class Budcont (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bcc = db.Column(db.Integer, unique = True)
    title = db.Column(db.String, unique = True)
    subhead = db.relationship('Subhead', backref='budget_of_subhead', lazy = 'dynamic')

class Ranks (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    rank = db.Column(db.String, unique = True)
    oder = db.Column(db.Integer)
    pers = db.relationship('Pers', backref = 'rank_of_pers', lazy = 'dynamic')

class Subhead (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bccid = db.Column(db.Integer, db.ForeignKey('budcont.id'))
    shc = db.Column(db.Integer, unique=True)
    descrip = db.Column(db.String, unique=True)
    trans = db.relationship('Trans', backref='subhead_of_trans', lazy = 'dynamic')

class Trans (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    amount = db.Column(db.Float)
    accid = db.Column(db.Integer, db.ForeignKey('acct.id'))
    subhid = db.Column(db.Integer, db.ForeignKey('subhead.id'))
    persid = db.Column(db.Integer, db.ForeignKey('pers.id'))
    unitid = db.Column(db.Integer, db.ForeignKey('units.id'))
    date = db.Column(db.String)
    auth = db.Column(db.String)
    remark = db.Column(db.String)
    admid = db.Column(db.Integer, db.ForeignKey('admn.id'))

class Units (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nam = db.Column(db.String, unique = True)
    comdid = db.Column(db.Integer, db.ForeignKey('comds.id'))
    locid = db.Column(db.Integer, db.ForeignKey('locs.id'))
    acct = db.relationship('Acct', backref = 'unit_of_acct', lazy = 'dynamic')
    trans = db.relationship('Trans', backref = 'unit_of_trans', lazy = 'dynamic')
    #__mapper_args__ = {"order_by":nam}