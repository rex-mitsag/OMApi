import sqlmodule.functions as fn

def returnLogin(input) :
    sqlquery = 'EXEC SelectUser @Mobile = '+str(input)
    return fn.getlistdata(sqlquery)

def getmenu(ipId, ipOpt) :
    sqlquery = "EXEC SelectMenu @Uid = '"+str(ipId)+"', @Opt = "+str(ipOpt)
    return fn.getlistdata(sqlquery)

def getpkgname(ipId) :
    sqlquery = "EXEC GetPackage @uid = '"+str(ipId)+"'"
    return fn.getlistdata(sqlquery)

def getledger(ipId) :
    sqlquery = "EXEC GetLedgerDetails @uid = '"+str(ipId)+"'"
    return fn.getlistdata(sqlquery)

def getflavor(inpID) :
    sqlquery = "EXEC GetFlavours @uid='"+str(inpID)+"'"
    return fn.getlistdata(sqlquery)

def getohmenu(inpID) :
    sqlquery = "EXEC SelectOHMenu @id='"+str(inpID)+"'"
    return fn.getlistdata(sqlquery)

def getSuperID(ipID) :
    sqlquery = "EXEC SelectSuper @dealer='"+str(ipID)+"'"
    return fn.getlistdata(sqlquery)

def getUsersToAuth(ipID, option, date) :
    sqlquery = "EXEC SelectSubToBeAuthAlt @uid='"+str(ipID)+"', @option='"+str(option)+"', @date='"+str(date)+"'"
    return fn.getlistdata(sqlquery)

def getdealersforss(ipID) :
    sqlquery = "EXEC SelectDealersForSuper @id='"+str(ipID)+"'"
    return fn.getlistdata(sqlquery)

def getfestival(date) :
    sqlquery = "EXEC SelectFestival @date='"+str(date)+"'"
    return fn.getlistdata(sqlquery)

def logout(inp, id) :
    sqlquery = "EXEC LogOut @input="+str(inp)+", @id='"+str(id)+"'"
    return fn.updatedata(sqlquery)

#--------NEW FUNCTIONS--------#

def register(pre, uname, mobile, aadhar, fname, fstatus, p1, p2, dname, oaddress, ostate, opin, gaddress, gstate, gpin, gst, pan, fssai, fsdate, dcode) :
    sqlquery = "EXEC RegisterUser @pre='"+str(pre)+"', @uname='"+str(uname)+"',	@mobile="+str(mobile)+", @aadhar='"+str(aadhar)+"',	@fname='"+str(fname)+"', @fstatus='"+str(fstatus)+"', @p1='"+str(p1)+"', @p2='"+str(p2)+"',	@dname='"+str(dname)+"', @oaddress='"+str(oaddress)+"',	@ostate='"+str(ostate)+"', @opin="+str(opin)+", @gaddress='"+str(gaddress)+"', @gstate='"+str(gstate)+"', @gpin="+str(gpin)+",	@gst='"+str(gst)+"', @pan='"+str(pan)+"', @fssai='"+str(fssai)+"',	@fsdate='"+str(fsdate)+"', @devicecode='"+str(dcode)+"'"
    return fn.getlistdata(sqlquery)

def loginuser(mode, value) :
    sqlquery = "EXEC LoginUser @mode="+str(mode)+", @value='"+str(value)+"'"
    return fn.getlistdata(sqlquery)

def getusermenu(ipId, ipOpt) :
    sqlquery = "EXEC SelectMainMenu @Uid = '"+str(ipId)+"', @Opt = "+str(ipOpt)
    return fn.getlistdata(sqlquery)

def getorderhistorymenu(inpID) :
    sqlquery = "EXEC SelectOrderHistoryMenu @id='"+str(inpID)+"'"
    return fn.getlistdata(sqlquery)

def getpkgdetails(ipId) :
    sqlquery = "EXEC SelectPackageDetails @uid = '"+str(ipId)+"'"
    return fn.getlistdata(sqlquery)

def getupperid(ipID) :
    sqlquery = "EXEC SelectUpperID @dealer='"+str(ipID)+"'"
    return fn.getlistdata(sqlquery)

def getledgerdetails(ipId) :
    sqlquery = "EXEC SelectLedgerDetails @uid = '"+str(ipId)+"'"
    return fn.getlistdata(sqlquery)

def getavailableflavour(inpID) :
    sqlquery = "EXEC SelectAvailableFlavours @uid='"+str(inpID)+"'"
    return fn.getlistdata(sqlquery)

def getdealername(ipID) :
    sqlquery = "EXEC SelectDealerNames @id='"+str(ipID)+"'"
    return fn.getlistdata(sqlquery)

def getsupername(ipID) :
    sqlquery = "EXEC SelectSuperNames @id='"+str(ipID)+"'"
    return fn.getlistdata(sqlquery)

def getordersforauth(ipID, list, option) :
    sqlquery = "EXEC SelectOrderForAuthorize @uid='"+str(ipID)+"', @list='"+str(list)+"', @option='"+str(option)+"'"
    return fn.getlistdata(sqlquery)

def getacceptedorders(ipID, list, option, date) :
    sqlquery = "EXEC SelectAcceptedOrder @uid='"+str(ipID)+"', @list='"+str(list)+"', @option='"+str(option)+"', @date='"+str(date)+"'"
    return fn.getlistdata(sqlquery)