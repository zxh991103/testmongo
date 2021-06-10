import pymongo

myclient = pymongo.MongoClient('mongodb://139.224.63.113:27017/')

mydb = myclient['datatest']


def loginuser(username, password):
    users = mydb["users"]
    for i in users.find():
        if username == i["username"] and password == i['password']:
            return True
    return False


def createuser(username, password):
    users = mydb["users"]
    for i in users.find():
        if username == i["username"]:
            return False
    newadmin = {
        "username": username,
        "password": password
    }
    x = users.insert_one(newadmin)

    return True


def showall():
    users = mydb["users"]
    print('all users:')
    for i in users.find():
        print(i)



if __name__ == '__main__':
    # createuser('user1','111')
    print(loginuser('user1','111'))
    showall()