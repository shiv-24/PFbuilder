from pymongo import MongoClient

def getMongoClient(ipAddress) :
    client = MongoClient(ipAddress)

    return client

def getcollection(client, db_name, coll_name):
    return client.get_database(db_name).get_collection(coll_name)

def getCollDataFindOne(client,db_name,coll_name):
    return client.get_database(db_name).get_collection(coll_name).find_one()

def insertData(client,db_name,coll_name, data):
    client.get_database(db_name).get_collection(coll_name).insert(data)

def getDataFindWithFiltersAndCustomFields(client,db_name,coll_name,filter,requiredFields,order):
    return client.get_database(db_name).get_collection(coll_name).find(filter,requiredFields).sort(order)

def getDataFindWithFiltersAllFields(client,db_name,coll_name,filter,order):
    return client.get_database(db_name).get_collection(coll_name).find(filter).sort(order)

def getDataFindWithoutFilters(client,db_name,coll_name,order):
    return client.get_database(db_name).get_collection(coll_name).find().sort(order)

def getDistinctValues(client,db_name,coll_name,distinct_fields):
    return client.get_database(db_name).get_collection(coll_name).distinct(distinct_fields)
