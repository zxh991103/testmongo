import pymongo

myclient = pymongo.MongoClient('mongodb://139.224.63.113:27017/')

mydb = myclient['datatest']

def loginau(username,password):


    admins = mydb["admins"]
    for i in admins.find():
        if username == i["username"] and password == i['password']:
            return True
    return False


def createadmin(username,password):

    admins = mydb["admins"]
    for i in admins.find():
        if username == i["username"]:
            return False
    newadmin = {
        "username" :username,
        "password" : password
    }
    x = admins.insert_one(newadmin)

    return True

def showall():
    admins = mydb["admins"]
    print('all administrator:')
    for i in admins.find():
        print(i)




