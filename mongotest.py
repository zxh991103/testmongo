import pymongo

myclient = pymongo.MongoClient('mongodb://139.224.63.113:27017/')

mydb = myclient['datatest']
mycol = mydb['sites']

collist = mydb. list_collection_names()

print(collist)



