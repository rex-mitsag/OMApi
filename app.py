import os
from flask import Flask, request
import json
import collections

import sqlmodule.functions as func
import sqlmodule.ordersql as osq
import sqlmodule.usersql as usq

app = Flask(__name__)

##-----------USER------------##

@app.route('/user/getUserData')
def validate() :
    mnum = str(request.args['mobile'])
    out = usq.returnLogin(mnum)
    jsonList = {
        "id" : out[0][0],
        "name" : out[0][1],
        "state" : out[0][2]
    }
    json_out = json.dumps(jsonList)
    return json_out
    
@app.route('/user/getMenu')
def getAllMenu() :
    uid = str(request.args['uid'])
    option = str(request.args['option'])
    out = usq.getmenu(uid, option)
    objects_list = []
    for row in out:
        d = collections.OrderedDict()
        d["menu"] = row[0]
        d["route"] = row[1]
        d["arg1"] = row[2]
        d["arg2"] = row[3]
        objects_list.append(d)
    jsonList = json.dumps(objects_list)
    return jsonList

@app.route('/user/getPkgName')
def getPkgName() :
    uid = str(request.args['uid'])
    out = usq.getpkgname(uid)
    objects_list = []
    for row in out :
        d = collections.OrderedDict()
        d["name"] = row[0]
        d["cost"] = row[1]
        objects_list.append(d)
    jsonList = json.dumps(objects_list)
    return jsonList

@app.route('/user/getLedger')
def getLedger() :
    uid = str(request.args['uid'])
    out = usq.getledger(uid)
    jsonList = {
        "minAmt" : out[0][0],
        "balance" :  out[0][1],
    }
    json_out = json.dumps(jsonList)
    return json_out

@app.route('/order/getFlavor')
def getFlavors() :
    uid = str(request.args['id'])
    out = usq.getflavor(uid)
    objects_list = []
    for row in out :
        d = collections.OrderedDict()
        d["name"] = row[0]
        objects_list.append(d)
    jsonList = json.dumps(objects_list)
    return jsonList

@app.route('/order/getAvailFlavor')
def getAvailFlavor() :
    uid = str(request.args['id'])
    out = usq.getavailableflavour(uid)
    objects_list = []
    for row in out :
        d = collections.OrderedDict()
        d["name"] = row[0]
        d["crt"] = row[1]
        d["ep"] = row[2]
        d["bag"] = row[3]
        objects_list.append(d)
    jsonList = json.dumps(objects_list)
    return jsonList

@app.route('/orderhistory/getOHMenu')
def getOHMenu() :
    uid = str(request.args['id'])
    out = usq.getohmenu(uid)
    objects_list = []
    for row in out :
        d = collections.OrderedDict()
        d["menu"] = row[0]
        d["route"] = row[1]
        d["arg"] = row[2]
        objects_list.append(d)
    jsonList = json.dumps(objects_list)
    return jsonList

@app.route('/user/getSuperior')
def getSuperId() :
    dealer = str(request.args['dealer'])
    out = usq.getSuperID(dealer)
    objects_list = []
    for row in out :
        d = collections.OrderedDict()
        d["id"] = row[0]
        d["name"] = row[1]
        objects_list.append(d)
    jsonList = json.dumps(objects_list)
    return jsonList

@app.route('/user/authUsers')
def authUsers() :
    id = str(request.args['id'])
    opt = str(request.args['option'])
    date = str(request.args['date'])
    out = usq.getUsersToAuth(id, opt, date)
    objects_list = []
    if len(out) == 0 :
        return '0'
    else :
        for row in out :
            d = collections.OrderedDict()
            d["id"] = row[0]
            d["name"] = row[1]
            d["ordid"] = row[2]
            d["basket"] = row[3]
            d["amount"] = row[4]
            d["CRT"] = row[5]
            d["EP"] = row[6]
            d["BAG"] = row[7]
            d["rem"] = row[8]
            d["forward"] = row[9]
            d["status"] = row[10]
            objects_list.append(d)
        jsonList = json.dumps(objects_list)
        return jsonList

@app.route('/user/getDealerSS')
def getDealerSS() :
    id = str(request.args['id'])
    out = usq.getdealersforss(id)
    objects_list = []
    for row in out :
        d = collections.OrderedDict()
        d["id"] = row[0]
        d["name"] = row[1]
        d["amount"] = row[2]
        d["date"] = row[3]
        objects_list.append(d)
    jsonList = json.dumps(objects_list)
    return jsonList

@app.route('/user/getFestivals')
def getFestivals() :
    date = str(request.args['date'])
    out = usq.getfestival(date)
    objects_list = []
    if len(out) == 0 :
        return '0'
    else :
        jsonList = {
            "festival" : out[0][0],  
        }
    json_out = json.dumps(jsonList)
    return json_out

@app.route('/user/logOutUser')
def logOutUser() :
    input = str(request.args['input'])
    id = str(request.args['id'])
    out = usq.logout(input, id)
    return str(out[0][0])

##-----------ORDER------------##

##-----------to be deleted-----------##

@app.route('/order/inputOrderId') 
def orderid() :
    orderid = str(request.args['id'])
    orderdate = str(request.args['date'])
    latitude = str(request.args['lat'])
    longitude = str(request.args['long'])
    amount = str(request.args['amt'])
    crt = str(request.args['crt'])
    ep = str(request.args['ep'])
    bag = str(request.args['bag'])
    rem = str(request.args['rem'])
    out = osq.inputorder(orderid, orderdate, latitude, longitude, amount, crt, ep, bag, rem)
    return str(out[0][0])

@app.route('/order/inputDealerOrderId') 
def dealerorderid() :
    sid = str(request.args['sid'])
    orderid = str(request.args['id'])
    orderdate = str(request.args['date'])
    latitude = str(request.args['lat'])
    longitude = str(request.args['long'])
    amount = str(request.args['amt'])
    crt = str(request.args['crt'])
    ep = str(request.args['ep'])
    bag = str(request.args['bag'])
    rem = str(request.args['rem'])
    out = osq.inputdealerorder(sid, orderid, orderdate, latitude, longitude, amount, crt, ep, bag, rem)
    return str(out[0][0])

@app.route('/order/getOrderBasket')
def getOrderBasket() :
    orderid = str(request.args['id'])
    bkt = str(request.args['basket'])
    out = osq.inputbasket(orderid, bkt)
    return str(out)

@app.route('/order/getOrderDetail')
def getOrderDetail() :
    orderid = str(request.args['id'])
    pkg = str(request.args['pkg'])
    mm = str(request.args['mm'])
    pd = str(request.args['pd'])
    km = str(request.args['km'])
    ct = str(request.args['ct'])
    tt = str(request.args['tt'])
    ctk = str(request.args['ctk'])
    am = str(request.args['am'])
    hj = str(request.args['hj'])
    co = str(request.args['co'])
    mix = str(request.args['mix'])
    epkg = str(request.args['epkg'])
    emm = str(request.args['emm'])
    epd = str(request.args['epd'])
    ekm = str(request.args['ekm'])
    ect = str(request.args['ect'])
    ett = str(request.args['ett'])
    ectk = str(request.args['ectk'])
    eam = str(request.args['eam'])
    ehj = str(request.args['ehj'])
    eco = str(request.args['eco'])
    emix = str(request.args['emix'])
    bpkg = str(request.args['bpkg'])
    bmm = str(request.args['bmm'])
    bpd = str(request.args['bpd'])
    bkm = str(request.args['bkm'])
    bct = str(request.args['bct'])
    btt = str(request.args['btt'])
    bctk = str(request.args['bctk'])
    bam = str(request.args['bam'])
    bhj = str(request.args['bhj'])
    bco = str(request.args['bco'])
    bmix = str(request.args['bmix'])
    out = osq.inputorderdetails(orderid, pkg, mm, pd, km, ct, tt, ctk, am, hj, co, mix, epkg, emm, epd, ekm, ect, ett, ectk, eam, ehj, eco, emix, bpkg, bmm, bpd, bkm, bct, btt, bctk, bam, bhj, bco, bmix)
    return str(out)


##-------------------------##

@app.route('/order/insertDealerOrder')
def insertDealerOrder() :
    sid = str(request.args['sid'])
    uid = str(request.args['id'])
    orderdate = str(request.args['date'])
    location = str(request.args['loc'])
    amount = str(request.args['amt'])
    crt = str(request.args['crt'])
    ep = str(request.args['ep'])
    bag = str(request.args['bag'])
    basket = str(request.args['basket'])
    rem = str(request.args['rem'])
    out = osq.ipdealerorder(sid, uid, orderdate, location, amount, crt, ep, bag, basket, rem)
    return str(out[0][0])

@app.route('/order/insertSuperOrder')
def insertSuperOrder() :
    uid = str(request.args['id'])
    orderdate = str(request.args['date'])
    location = str(request.args['loc'])
    amount = str(request.args['amt'])
    crt = str(request.args['crt'])
    ep = str(request.args['ep'])
    bag = str(request.args['bag'])
    basket = str(request.args['basket'])
    rem = str(request.args['rem'])
    out = osq.ipsuperorder(uid, orderdate, location, amount, crt, ep, bag, basket, rem)
    return str(out[0][0])

@app.route('/order/insertOrderDetail')
def insertOrderDetail() :
    orderid = str(request.args['id'])
    pkg = str(request.args['pkg'])
    mm = str(request.args['mm'])
    pd = str(request.args['pd'])
    km = str(request.args['km'])
    ct = str(request.args['ct'])
    tt = str(request.args['tt'])
    ctk = str(request.args['ctk'])
    am = str(request.args['am'])
    hj = str(request.args['hj'])
    co = str(request.args['co'])
    mix = str(request.args['mix'])
    epkg = str(request.args['epkg'])
    emm = str(request.args['emm'])
    epd = str(request.args['epd'])
    ekm = str(request.args['ekm'])
    ect = str(request.args['ect'])
    ett = str(request.args['ett'])
    ectk = str(request.args['ectk'])
    eam = str(request.args['eam'])
    ehj = str(request.args['ehj'])
    eco = str(request.args['eco'])
    emix = str(request.args['emix'])
    bpkg = str(request.args['bpkg'])
    bmm = str(request.args['bmm'])
    bpd = str(request.args['bpd'])
    bkm = str(request.args['bkm'])
    bct = str(request.args['bct'])
    btt = str(request.args['btt'])
    bctk = str(request.args['bctk'])
    bam = str(request.args['bam'])
    bhj = str(request.args['bhj'])
    bco = str(request.args['bco'])
    bmix = str(request.args['bmix'])
    out = osq.inputorderdetails(orderid, pkg, mm, pd, km, ct, tt, ctk, am, hj, co, mix, epkg, emm, epd, ekm, ect, ett, ectk, eam, ehj, eco, emix, bpkg, bmm, bpd, bkm, bct, btt, bctk, bam, bhj, bco, bmix)
    return str(out)

##-------------------------##


##-----------to be deleted-----------##

@app.route('/orderhistory/getOrderByDate')
def checkDate() :
    id = str(request.args['id'])
    date = str(request.args['date'])
    out = osq.checkdate(id, date)
    objects_list = []
    if len(out) == 0 :
        return '0'
    else :
        for row in out :
            d = collections.OrderedDict()
            d["id"] = row[0]
            d["status"] = row[1]
            d["crt"] = row[2]
            d["ep"] = row[3]
            d["bag"] = row[4]
            d["date"] = row[5]
            d["basket"] = row[6]
            d["remark"] = row[7]
            objects_list.append(d)
        jsonList = json.dumps(objects_list)
        return jsonList

@app.route('/orderhistory/getSubOrderByDate')
def checkSubDate() :
    id = str(request.args['id'])
    date = str(request.args['date'])
    out = osq.checksubdate(id, date)
    objects_list = []
    if(len(out) == 0) :
        return '0'
    else :
        for row in out :
            d = collections.OrderedDict()
            d["id"] = row[0]
            d["status"] = row[1]
            d["name"] = row[2]
            d["crt"] = row[3]
            d["ep"] = row[4]
            d["bag"] = row[5]
            d["date"] = row[6]
            d["basket"] = row[7]
            d["remark"] = row[8]
            objects_list.append(d)
        jsonList = json.dumps(objects_list)
        return jsonList


##-----------------------------##

@app.route('/orderhistory/getDirectOrder')
def getDirectOrder() :
    id = str(request.args['id'])
    start = str(request.args['start'])
    end = str(request.args['end'])
    out = osq.directorder(id, start, end)
    objects_list = []
    if len(out) == 0 :
        return '0'
    else :
        for row in out :
            d = collections.OrderedDict()
            d["id"] = row[0]
            d["forward"]  = row[1]
            d["status"] = row[2]
            d["crt"] = row[3]
            d["ep"] = row[4]
            d["bag"] = row[5]
            d["basket"] = row[6]
            d["date"] = row[7]
            d["remark"] = row[8]
            objects_list.append(d)                  
        jsonList = json.dumps(objects_list)
        return jsonList

@app.route('/orderhistory/getDealerOrder')
def getDealerOrder() :
    id = str(request.args['id'])
    start = str(request.args['start'])
    end = str(request.args['end'])
    option = str(request.args['option'])
    out = osq.dealerorder(id, start, end, option)
    objects_list = []
    if(len(out) == 0) :
        return '0'
    else :
        for row in out :
            d = collections.OrderedDict()
            d["id"] = row[0]
            d["forward"]  = row[1]
            d["status"] = row[2]
            d["name"] = row[3]
            d["crt"] = row[4]
            d["ep"] = row[5]
            d["bag"] = row[6]            
            d["basket"] = row[7]
            d["date"] = row[8]
            d["remark"] = row[9]
            objects_list.append(d)
        jsonList = json.dumps(objects_list)
        return jsonList

@app.route('/order/updateLedger')
def updateLedger() :
    id = str(request.args['id'])
    ledger = str(request.args['ledger'])
    out = osq.updateledger(id, ledger)
    return str(out)

@app.route('/order/updateDBalance')
def updateDBalance() :
    id = str(request.args['id'])
    ledger = str(request.args['ledger'])
    date = str(request.args['date'])
    added = str(request.args['added'])
    out = osq.updatedailybalance(id, ledger, date, added)
    return str(out)

@app.route('/order/getOrderDetails')
def getOrderDetails() :
    oid = str(request.args['oid'])
    out = osq.getorderdetails(oid)
    objects_list = []
    for row in out :
        d = collections.OrderedDict()
        d["pkg"] = row[0]
        d["mm"] = row[1]
        d["tp"] = row[2]
        d["km"] = row[3]
        d["ct"] = row[4]
        d["tt"] = row[5]
        d["ctk"] = row[6]
        d["am"] = row[7]
        d["hj"] = row[8]
        d["co"] = row[9]
        d["mix"] = row[10]
        objects_list.append(d)
    jsonList = json.dumps(objects_list)
    return jsonList

@app.route('/order/updateUserAuth')
def updateUserAuth() :
    auth = str(request.args['auth'])
    rem = str(request.args['remarks'])
    oid = str(request.args['oid'])
    out = osq.updateauth(auth, rem, oid)
    return str(out)

@app.route('/order/deleteOrder')
def deleteOrder() :
    oid = str(request.args['oid'])
    id = str(request.args['id'])
    out = osq.deleteord(oid, id)
    return str(out)

@app.route('/order/countOrder')
def countOrder() :
    id = str(request.args['id'])
    date = str(request.args['date'])
    out = osq.countord(id, date)
    return str(out[0][0])

##-----------MAIN------------##

if __name__ == '__main__' :
    app.run()