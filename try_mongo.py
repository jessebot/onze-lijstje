#!/usr/bin/env python3
import pymongo

# we're using localhost for now
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# new db
mydb = myclient["mygroceries"]
print(myclient.list_database_names())

# create a collection - like a table?
mycol = mydb["groceries"]
print(mydb.list_collection_names())
# res = mycol.create_index('name', unique=True)

# insert a grocery
my_groceries_dict = {"name": "dates",
                     "category": "fruit"}
x = mycol.insert_one(my_groceries_dict)

# check for the result
for x in mycol.find():
    print(x)

