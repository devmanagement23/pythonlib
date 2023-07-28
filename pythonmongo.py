# 1 connection to mongodb
import pymongo

# server location
myclient = pymongo.MongoClient("mongodb://localhost:27017")

# making database
isrodatabase = myclient["isrodatabase"]

# making collection
staffcollection = isrodatabase["staffcollection"]

# making enteries as dictionaries
scientistsdict = { "name": "Rakesh Kumar", "position":"Director","division": "Liquid Propulsion Systems","Location":"Thiruvanthapuram" }

# inserting the entry -- this return the id of the object
x = staffcollection.insert_one(scientistsdict)

print(x.inserted_id)

# remaining codes are on page 2