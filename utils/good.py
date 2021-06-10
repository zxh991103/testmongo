import pymongo

myclient = pymongo.MongoClient('mongodb://139.224.63.113:27017/')

mydb = myclient['datatest']

'''
goods:
    id
    name
    price
    contain # 余量
    salenumber # 销量
    userreview :
        username
        review_string
'''

def addgoods(id,name,price,contain):
    goods = mydb["goods"]
    for i in goods.find():
        if id == i["id"]:
            return False
    newgood = {
        "id":id,
        "name":name,
        "price":price,
        "contain":contain,
        "photopath":'http://139.224.63.113/photo/'+id+'.jpg',
        "salenumber":0,
        "userreview":{

        }
    }
    x = goods.insert_one(newgood)
    return True

def deletegoods(id):
    goods = mydb["goods"]

    newgood = {
        "id":id
    }
    x = goods.delete_one(newgood)

    return True


def showall():
    goods = mydb["goods"]
    print('all goods:')
    for i in goods.find():
        print(i)

if __name__ == '__main__':
    # addgoods('1','鞋',100,1000)
    # deletegoods('1')
    showall()