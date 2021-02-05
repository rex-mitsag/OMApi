import sqlmodule.functions as fn

def inputorder(inputID, inputDate, inputlat, inputlong, inputAmt, crt, ep, bag, rem) :  
    sqlquery = "EXEC SelectOrder @uid = '"+str(inputID)+"', @date = '"+str(inputDate)+"', @lat = '"+str(inputlat)+"', @long = '"+str(inputlong)+"', @amt= "+str(inputAmt)+", @crt= "+str(crt)+", @ep= "+str(ep)+", @bag= "+str(bag)+", @rem='"+str(rem)+"'"
    return fn.getlistdata(sqlquery)

def inputdealerorder(inputSID, inputID, inputDate, inputlat, inputlong, inputAmt, crt, ep, bag, rem) :
    sqlquery = "EXEC SelectDealerOrder @sid='"+str(inputSID)+"', @uid = '"+str(inputID)+"', @date = '"+str(inputDate)+"', @lat = '"+str(inputlat)+"', @long = '"+str(inputlong)+"', @amt="+str(inputAmt)+", @crt= "+str(crt)+", @ep= "+str(ep)+", @bag= "+str(bag)+", @rem='"+str(rem)+"'"
    return fn.getlistdata(sqlquery)

def inputorderdetails(id, pkg, mm, pd, km, ct, tt, ctk, am, hj, co, mix, epkg, emm, epd, ekm, ect, ett, ectk, eam, ehj, eco, emix, bpkg, bmm, bpd, bkm, bct, btt, bctk, bam, bhj, bco, bmix) :
    sqlquery = "EXEC InsertOrderDetails @id='"+str(id)+"', @pkg='"+str(pkg)+"', @mm="+str(mm)+", @pd="+str(pd)+", @km="+str(km)+", @ct="+str(ct)+", @tt="+str(tt)+", @ctk="+str(ctk)+", @am="+str(am)+", @hj="+str(hj)+", @co="+str(co)+", @mix="+str(mix)+", @epkg='"+str(epkg)+"', @emm="+str(emm)+", @epd="+str(epd)+", @ekm="+str(ekm)+", @ect="+str(ect)+", @ett="+str(ett)+", @ectk="+str(ectk)+", @eam="+str(eam)+", @ehj="+str(ehj)+", @eco="+str(eco)+", @emix="+str(emix)+", @bpkg='"+str(bpkg)+"', @bmm="+str(bmm)+", @bpd="+str(bpd)+", @bkm="+str(bkm)+", @bct="+str(bct)+", @btt="+str(btt)+", @bctk="+str(bctk)+", @bam="+str(bam)+", @bhj="+str(bhj)+", @bco="+str(bco)+", @bmix="+str(bmix)
    return fn.updatedata(sqlquery)

def inputbasket(id, basket) :
    sqlquery = "EXEC inputBasket @id='"+str(id)+"', @amt="+str(basket)
    return fn.updatedata(sqlquery)

def updateledger(id, ledger) :
    sqlquery = "EXEC UpdateLedger @ledger="+str(ledger)+", @uid='"+str(id)+"'"
    return fn.updatedata(sqlquery)

def updatedailybalance(id, ledger, date, added) :
    sqlquery = "EXEC UpdateDailyBalance @ledger="+str(ledger)+", @uid='"+str(id)+"', @added="+str(added)+", @date='"+str(date)+"'"
    return fn.updatedata(sqlquery)

def getorderdetails(oid) :
    sqlquery = "EXEC SelectOrderDetails @oid='"+str(oid)+"'"
    return fn.getlistdata(sqlquery)

def updateauth(ip, rem, oid) :
    sqlquery = "EXEC UpdateAuth @auth='"+str(ip)+"', @remark='"+str(rem)+"', @ordid='"+str(oid)+"'"
    return fn.updatedata(sqlquery)



##----NEW FUNCTIONS----##

def updateordauth(ip, rem, oid, uname, utype) :
    sqlquery = "EXEC UpdateOrdAuthorization @auth='"+str(ip)+"', @remark='"+str(rem)+"', @ordid='"+str(oid)+"', @uname='"+str(uname)+"', @utype='"+str(utype)+"'"
    return fn.updatedata(sqlquery)

def ipsuperorder(inputID, inputDate, inputloc, inputAmt, crt, ep, bag, basket, rem) :
    sqlquery = "EXEC InsertSuperOrder @uid = '"+str(inputID)+"', @date = '"+str(inputDate)+"', @loc = '"+str(inputloc)+"', @amt= "+str(inputAmt)+", @crt= "+str(crt)+", @ep= "+str(ep)+", @bag= "+str(bag)+", @basket="+str(basket)+", @rem='"+str(rem)+"'"
    return fn.getlistdata(sqlquery)

def ipdealerorder(inputSID, inputID, inputDate, inputloc, inputAmt, crt, ep, bag, basket, rem) :
    sqlquery = "EXEC InsertDealerOrder @sid='"+str(inputSID)+"', @uid = '"+str(inputID)+"', @date = '"+str(inputDate)+"', @loc = '"+str(inputloc)+"', @amt="+str(inputAmt)+", @crt= "+str(crt)+", @ep= "+str(ep)+", @bag= "+str(bag)+", @basket="+str(basket)+", @rem='"+str(rem)+"'"
    return fn.getlistdata(sqlquery)

def inputflavororderdetails(id, pkg, mm, pd, km, ct, tt, ctk, am, hj, co, mix, epkg, emm, epd, ekm, ect, ett, ectk, eam, ehj, eco, emix, bpkg, bmm, bpd, bkm, bct, btt, bctk, bam, bhj, bco, bmix) :
    sqlquery = "EXEC InsertFlavorOrderDetails @id='"+str(id)+"', @pkg='"+str(pkg)+"', @mm="+str(mm)+", @pd="+str(pd)+", @km="+str(km)+", @ct="+str(ct)+", @tt="+str(tt)+", @ctk="+str(ctk)+", @am="+str(am)+", @hj="+str(hj)+", @co="+str(co)+", @mix="+str(mix)+", @epkg='"+str(epkg)+"', @emm="+str(emm)+", @epd="+str(epd)+", @ekm="+str(ekm)+", @ect="+str(ect)+", @ett="+str(ett)+", @ectk="+str(ectk)+", @eam="+str(eam)+", @ehj="+str(ehj)+", @eco="+str(eco)+", @emix="+str(emix)+", @bpkg='"+str(bpkg)+"', @bmm="+str(bmm)+", @bpd="+str(bpd)+", @bkm="+str(bkm)+", @bct="+str(bct)+", @btt="+str(btt)+", @bctk="+str(bctk)+", @bam="+str(bam)+", @bhj="+str(bhj)+", @bco="+str(bco)+", @bmix="+str(bmix)
    return fn.updatedata(sqlquery)

def ippaymentdetails(uid, date, utr, amt) :
    sqlquery = "EXEC InsertPayment @uid='"+str(uid)+"', @date='"+str(date)+"', @utr='"+str(utr)+"', @amt="+str(amt)
    return fn.updatedata(sqlquery)

def updatebalance(id, ledger) :
    sqlquery = "EXEC UpdateBalance @ledger="+str(ledger)+", @uid='"+str(id)+"'"
    return fn.updatedata(sqlquery)

def selectorderdetails(oid) :
    sqlquery = "EXEC SelectOrderFlavorDetails @oid='"+str(oid)+"'"
    return fn.getlistdata(sqlquery)

def deleteord(oid, id) :
    sqlquery = "EXEC DeleteOrder @ordid='"+str(oid)+"', @id='"+str(id)+"'"
    return fn.updatedata(sqlquery)

def countord(id, date) :
    sqlquery = "EXEC CountOrders @uid='"+str(id)+"', @date='"+str(date)+"'"
    return fn.getlistdata(sqlquery)

##------------------------------------------##




##direct
def checkdate(id, date) :
    sqlquery = "EXEC checkOrder @date='"+str(date)+"', @id='"+str(id)+"'"
    return fn.getlistdata(sqlquery)

def directorder(id, start, end) :
    sqlquery = "EXEC SelectDirectOrdersHistory @id='"+str(id)+"', @start='"+str(start)+"', @end='"+str(end)+"'"
    return fn.getlistdata(sqlquery)


##dealer
def checksubdate(id, date) :
    sqlquery = "EXEC checkSubOrder @date='"+str(date)+"', @id='"+str(id)+"'"
    return fn.getlistdata(sqlquery)

def dealerorder(id, start, end, option) :
    sqlquery = "EXEC SelectDealerOrdersHistory @id='"+str(id)+"', @start='"+str(start)+"', @end='"+str(end)+"', @option='"+str(option)+"'"
    return fn.getlistdata(sqlquery)


##super
def superorder(id, start, end, option) :
    sqlquery = "EXEC SelectSuperOrdersHistory @id='"+str(id)+"', @start='"+str(start)+"', @end='"+str(end)+"', @option='"+str(option)+"'"
    return fn.getlistdata(sqlquery)
