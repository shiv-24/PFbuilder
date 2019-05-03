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
