from flask import Blueprint, render_template, url_for, request

from finas.db import * # Acct, Comds, Locs, Pers, Ranks, Units

import requests

clerk = Blueprint('clerk', __name__, url_prefix='/clerk')

@clerk.route('/add-acct', methods = ['POST','GET'])
def add_acct():
    if request.method=='POST':
        res = requests.post(url_for('api._acct', _external = True), json=request.form.to_dict())
        return res.json()
    units = Units.query.all()
    return render_template('add-acct.html', units = units)

@clerk.route('/add-budc', methods = ['POST', 'GET'])
def add_budc():
    if request.method == 'POST':
        res = requests.post(url_for('api.budc', _external=True ), json=request.form.to_dict())
        return res.json()
    return render_template('add-bud.html')

@clerk.route('/add-comd', methods = ['POST','GET'])
def add_comd():
    if request.method=='POST':
        response = requests.post(url_for('api.comd', _external = True), json=request.form.to_dict())
        return response.json()
    locs = Locs.query.all()
    return render_template('add-comd.html', locs = locs)

@clerk.route('/add-loc', methods = ['POST','GET'])
def add_loc():
    if request.method=='POST':
        response = requests.post(url_for('api._loc', _external = True), json=request.form.to_dict())
        return response.json()
    return render_template('add-loc.html')

@clerk.route('/add-pers', methods=['POST', 'GET'])
def add_pers():
    if request.method == 'POST':
        response = requests.post(url_for('api._pers', _external=True), json=request.form.to_dict())
        return response.json()
    ranks = Ranks.query.order_by(Ranks.oder).all()
    return render_template('add-pers.html', ranks=ranks)

@clerk.route('/add-subh', methods = ['POST','GET'])
def add_subh():
    if request.method=='POST':
        resp = requests.post(url_for('api.subh', _external = True), json=request.form.to_dict())
        return resp.json()
    budcs = Budcont.query.all()
    return render_template('add-subh.html', budcs = budcs)

@clerk.route('/new-trans', methods = ['POST','GET'])
def new_trans():
    if request.method == 'POST':
        response = requests.post(url_for('api._trans', _external=True), json=request.form.to_dict())
        return response.json()
    accts = Acct.query.all()
    purps = db.session.query(Budcont.bcc.label('code'), Subhead.id, Subhead.shc, Subhead.descrip).join(Subhead, Budcont.id==Subhead.bccid).all()
    # pers = Pers.query.all()
    pers = db.session.query(Pers.id, Pers.fnam, Pers.onam, Pers.snam, Pers.svcn, Ranks.rank).join(Ranks, Ranks.id==Pers.rankid).order_by(Ranks.oder, Pers.svcn).all()
    units = Units.query.all()
    return render_template('new-trans.html', accts = accts, purps=purps, pers = pers, units = units)

@clerk.route('/pend-trans', methods = ['POST','GET'])
def pend_trans():
    if request.method == 'GET':
        response = requests.post(url_for('api._trans', _external=True), json=request.form.to_dict())
        return response.json()
    return render_template('pend-trans.html')

@clerk.route('/add-unit', methods = ['POST','GET'])
def add_unit():
    if request.method=='POST':
        response = requests.post(url_for('api.units', _external = True), json=request.form.to_dict())
        return response.json()
    locs = requests.get(url_for('api._loc', _external = True), json={}).json()
    comds = requests.get(url_for('api.comd', _external = True), json={}).json()
    return render_template('add-unit.html', locs = locs, comds = comds)
