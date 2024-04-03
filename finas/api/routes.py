
'''
api
--------------
'''
from flask import Blueprint, request, render_template, redirect, url_for

from finas.marshmallow import AcctSchema, AdmnSchema, BudcSchema, ComdsSchema, LocsSchema, PersSchema, RanksSchema, SubhSchema, TranSchema, UnitsSchema

from sqlalchemy import exc

from finas.db import *

api = Blueprint('api', __name__, url_prefix='/api')

acct_schema = AcctSchema()
accts_schema = AcctSchema(many = True)

budc_schema = BudcSchema()
budcs_schema = BudcSchema(many=True)

comd_schema = ComdsSchema()
comds_schema = ComdsSchema(many=True)

loc_schema = LocsSchema()
locs_schema = LocsSchema(many=True)

per_schema = PersSchema()
pers_schema = PersSchema(many=True)

rank_schema = RanksSchema()
ranks_schema = RanksSchema(many = True)

subh_schema = SubhSchema()
subhs_schema = SubhSchema(many=True)

tran_schema = TranSchema()
trans_schema = TranSchema(many=True)

unit_schema = UnitsSchema()
units_schema = UnitsSchema(many=True)

#REg Acc
@api.route('/acct', methods = ['POST', 'GET'])
def _acct():
    # nam = request.json.get('nam')
    # descrip = request.json.get('descrip')
    # acctunit = request.json.get('acctunit')

    if request.method == 'POST':
        try:
            new_acct = Acct(**request.json)
            db.session.add(new_acct)
            db.session.commit()
            return acct_schema.jsonify(new_acct)
        except exc.IntegrityError:
            db.session.rollback()
            return {'error':'Acct reg failed, try again later'}
    accts = Acct.query.filter_by(**request).all()
    return accts_schema.jsonify(accts)

    # if request.method == 'GET':
    #     data = {}
    #     all_acct = Acct.query.all()
    #     for acct in all_acct:
    #         data[acct.id] = {'acctnam':acct.nam, 'descrip':acct.descrip, 'acctunit':acct.unitid}
    #     return data

@api.route('/admin', methods=['POST', 'GET'])
def admin():
    if request.method == 'POST':
        persid = request.json.get('persid')
        username = request.json.get('username')
        password = request.json.get('password')
        level = request.json.get('level')
        new_admin = Admn(persid=persid, usern=username, level=level)
        db.session.add(new_admin)
        new_admin.set_password(password)
        db.session.commit()
        return {'status':'success'}

@api.route('/budc', methods = ['POST', 'GET'])
def budc():
    if request.method == 'POST':
        try:
            new_budc = Budcont(**request.json)
            db.session.add(new_budc)
            db.session.commit()
            return budc_schema.jsonify(new_budc)
        except exc.IntegrityError:
            db.session.rollback()
            return {'error':'Budget Control Already Exists'}
    budcs = Budcont.query.filter_by(**request.json).order_by(Budcont.bcc).all()
    return budcs_schema.jsonify(budcs)

@api.route('/comd', methods=['POST', 'GET'])
def comd():
    if request.method == "POST":
        try:
            new_comd = Comds(**request.json)
            db.session.add(new_comd)
            db.session.commit()
            return comd_schema.jsonify(new_comd)
        except exc.IntegrityError:
            db.session.rollback()
            return {'error':'Command already exist'}
    comds = Comds.query.filter_by(**request.json).order_by(Comds.order).all()
    return comds_schema.jsonify(comds)

@api.route('/loc', methods=['POST', 'GET'])
def _loc():
    if request.method == "POST":
        try:
            new_loc = Locs(**request.json)
            db.session.add(new_loc)
            db.session.commit()
            return loc_schema.jsonify(new_loc)
        except exc.IntegrityError:
            db.session.rollback()
            return {'error':'Location already exist'}
    locs = Locs.query.filter_by(**request.json).order_by(Locs.locnam).all()
    return locs_schema.jsonify(locs)

#Staf reg
@api.route('/pers', methods=['POST', 'GET'])
def _pers():
    # svcn = request.json.get('svcn')
    # snam = request.json.get('snam')
    # fnam = request.json.get('fnam')
    # onam = request.json.get('onam')
    # rank = request.json.get('rank')
    if request.method == "POST":
        try:
            new_pers = Pers(**request.json)
            db.session.add(new_pers)
            db.session.commit()
            return per_schema.jsonify(new_pers)
        except exc.IntegrityError:
            db.session.rollback()
            return {'error':'Personel already exist'}
    pers = Pers.query.filter_by(**request.json).all()
    return pers_schema.jsonify(pers)


@api.route('/rank', methods=['POST', 'GET'])
def rank():
    if request.method == 'POST':
        # order = request.json.get('oder')
        # rank = request.json.get('rank')
        # new_rank = Ranks(oder=order, rank=rank)
        # db.session.add(new_rank)
        # db.session.commit()
        # return {'status':'success'}

        try:
            new_rank = Ranks(**request.json)
            db.session.add(new_rank)
            db.session.commit()
            return rank_schema.jsonify(new_rank)
        except exc.IntegrityError:
            db.session.rollback()
            return {'error':'Rank reg failed'}
    ranks = Ranks.query.filter_by(**request.json).all()
    return ranks_schema.jsonify(ranks)

@api.route('/subh', methods = ['POST', 'GET'])
def subh():
    if request.method == 'POST':
        try:
            new_subh = Subhead(**request.json)
            db.session.add(new_subh)
            db.session.commit()
            return subh_schema.jsonify(new_subh)
        except exc.IntegrityError:
            db.session.rollback()
            return {'error':'Subhead Already Exists'}
    subhs = Subhead.query.filter_by(**request.json).order_by(Subhead.shc).all()
    return subhs_schema.jsonify(subhs)

#trans
@api.route('/trans', methods=['POST', 'GET'])
def _trans():
    # persid = request.json.get('persid')
    # amount = request.json.get('amount')
    # accid = request.json.get('accid')
    # purpose = request.json.get('purpose')
    # date = request.json.get('date')
    # auth = request.json.get('auth')
    # admid = request.json.get('admid')

    if request.method == "POST":
        try:
            new_trans = Trans(**request.json)
            db.session.add(new_trans)
            db.session.commit()
            return tran_schema.jsonify(new_trans)
        except exc.IntegrityError:
            db.session.rollback()
            return {'error':'transaction failed'}
    trans = Trans.query.filter_by(**request.json).all()
    return trans_schema.jsonify(trans)

#trans
@api.route('/units', methods=['POST', 'GET'])
def units():
    if request.method == "POST":
        try:
            new_unit = Units(**request.json)
            db.session.add(new_unit)
            db.session.commit()
            return unit_schema.jsonify(new_unit)
        except exc.IntegrityError:
            db.session.rollback()
            return {'error':'Unit Already Exist'}
    units = Units.query.filter_by(**request.json).all()
    return units_schema.jsonify(units)