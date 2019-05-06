import Files.ConnectMongo as MC

client = MC.getMongoClient('127.0.0.1:27017')

# dbCur = MC.getDataFindWithFiltersAndCustomFields(client,'market_data','stock_data',{'Ticker':'AAPL'},{'CompanyName':1,'Date':1,'_id':0},[('Date',1)])
# for docs in dbCur:
#     print(docs)

# disStockVal  =   MC.getDistinctValues(client,'market_data','stock_data',"Ticker")

# disStockVal  =   MC.getDistinctValues(client,'market_data','benchmark_data',"BenchmarkTicker")

data = []

def findDataWithFilters_CustomFields(db_name,coll_name,filters,requiredFields,order):
    data   = MC.getDataFindWithFiltersAndCustomFields(client,db_name,coll_name,filters,requiredFields,order)
    return data

def findDataWithFilters_AllFields(db_name,coll_name,filters,order):
    data = MC.getDataFindWithFiltersAllFields(client,db_name,coll_name,filters,order)
    return data

def findDataWithoutFilters(db_name,coll_name,order):
    data = MC.getDataFindWithoutFilters(client,db_name,coll_name,order)
    return data

def getDistinctValues(db_name,coll_name,attributes):
    data = MC.getDistinctValues(client,db_name,coll_name,attributes)
    return data