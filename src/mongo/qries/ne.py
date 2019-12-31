# Requires pymongo 3.6.0+
from pymongo import MongoClient

client = MongoClient("mongodb://host:port/")
database = client["proxy"]
collection = database["proxies"]

# Created with Studio 3T, the IDE for MongoDB - https://studio3t.com/

query = {}
query["https_flag"] = {
    u"$ne": u"yes"
}


cursor = collection.find(query)
try:
    for doc in cursor:
        print(doc)
finally:
    client.close()
