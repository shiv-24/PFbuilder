from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL  >> to reflect your own connection string
# client = MongoClient('127.0.0.1:27017')
# db=client.admin
# Issue the serverStatus command and print the results
# serverStatusResul=db.command("serverStatus")
# pprint(serverStatusResul)

# db = client.get_database('test_2');
# print(db.get_collection('testing_1').find().next());

def getMongoClient(ipAddress):
    client= MongoClient(ipAddress)
    return client

def getCollection(client,db_name,coll_name):
    return client.get_database(db_name).get_collection(coll_name)

def getCollDataFindOne(client,db_name,coll_name):
    return client.get_database(db_name).get_collection(coll_name).find_one()

def insertData(client,db_name,coll_name, data):
    client.get_database(db_name).get_collection(coll_name).insert(data)
