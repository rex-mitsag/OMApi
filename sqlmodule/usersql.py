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

def getpkgcost() :
    sqlquery = "EXEC GetPkgCost"
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

def getUsersToAuth(ipID) :
    sqlquery = "EXEC SelectSubToBeAuthAlt @uid='"+str(ipID)+"'"
    return fn.getlistdata(sqlquery)

def getdealersforss(ipID) :
    sqlquery = "EXEC SelectDealersForSuper @id='"+str(ipID)+"'"
    return fn.getlistdata(sqlquery)

def getfestival(date) :
    sqlquery = "EXEC GetFestival @date='"+str(date)+"'"
    return fn.getlistdata(sqlquery)

def getdoom() :
    return 'DOOM Eternal'