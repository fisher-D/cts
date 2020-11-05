import datastruct as st
import database as db
import cryptos as cp
import hashlib
import base64
import time
# 献血者接口
# 包括注册，登录，和查询三个功能


class Blood_donor(object):
    pass
    # def register(self):
    #     pass

    # def login(self):
    #     pass

    # def queryCerti(self):

    #     pass

    # 献血站接口
    # 包含注册，登录，生成献血信息，推送信息四个功能
    # 推送信息：将生成的纪录推送到区块链上


class Station(object):
    location = "瓜园采血站"

    # def register(self):
    #     pass

    # def login(self):
    #     pass

    # def broadcastInfo(self):
    #     pass


def queryCerti(name, password):

    pass


def makeBloodInfo(object):
    time_stamp = time.strftime(
        '%Y-%m-%d-%H-%M-%S',
        time.localtime(time.time()))
    object["timeStamp"] = time_stamp
    hashcode = hashgenerator(object)
    object["bHashCode"] = hashcode
    db.blood_info.insert_one(object)
    del object["name"]
    del object["cType"]
    del object["idNum"]
    for x in object:
        print(x, object[x])


# 医院接口
# 包含注册，登录
# 血液入库信息，血液出库信息
# 推送信息五个功能
# 推送信息：将生成的纪录推送到区块链上


class Hospital(object):
    # def register(self):
    #     pass

    # def login(self):
    #     pass
    # 使用医院编码，和血液信息hash
    def in_blood_info(self, bcode):
        in_info = {}
        # query = {"bHashCode": self}
        # b_info = db.blood_info.find(query)
        in_info["inHashCode"] = ""
        in_info["bHashCode"] = bcode
        if self in st.chospital:
            in_info["chosptial"] = st.chospital[self]
            time_stamp = time.strftime(
                '%Y-%m-%d-%H-%M-%S',
                time.localtime(time.time()))
            in_info["timeStamp"] = time_stamp
            in_hash = hashgenerator(in_info)
            in_info["inHashCode"] = in_hash
            db.in_infos.insert_one(in_info)
            print(in_info)
        else:
            print("error")

    # 使用血液信息hash
    def out_blood_info(self):
        # out_info = {}
        query = {"bHashCode": self}
        res = db.in_infos.find(query)
        if res.count() != 0:
            for x in res:
                print(x)
        else:
            print("Not in the database")

        # out_info["outHashCode"] = ""
        # out_info["inHashCode"] = res["inHashCode"]
        # out_info["bHashCode"] = self
        # time_stamp = time.strftime(
        #     '%Y-%m-%d-%H-%M-%S',
        #     time.localtime(time.time()))
        # out_info["timeStamp"] = time_stamp
        # out_info["outHashCode"] = hashgenerator(out_info)
        # print(out_info)

    # 使用入库信息医院和入库信息hash
    def makeCerti(self, hospital):
        query = {"bHashCode": hospital}
        projectionFields = {'_id': False}
        res = db.blood_info.find(query, pojection=projectionFields)
        if len(res) != 0:
            certi = {}
            certi["inHashCode"] = hospital
            certi["chospital"] = st.chospital[self]
            time_stamp = time.strftime(
                '%Y-%m-%d-%H-%M-%S',
                time.localtime(time.time()))
            certi["timeStamp"] = time_stamp
            certi["BloodInfo"] = res
            print(certi)
        else:
            print("No record in Database")

    # def broadcastInfo(self):
    #     pass


def register(object):
    # def register(n, p, i, ph, pr, ch, sa):
    if object[4] != True:
        newDonor = {
            "name": object[0],
            "password": object[1],
            "idNum": object[2],
            "phone": object[3]
        }
        db.donorcol.insert_one(newDonor)
        res = db.donorcol.find({}, {"name"})
        for x in res:
            print(x)

    else:
        newDonor = {
            "name": object[0],
            "password": object[1],
            "idNum": object[2],
            "phone": object[3],
            "principal": object[4],
            "chospital": st.chospital[object[5]],
            "saddress": st.saddress[object[6]]
        }
        db.prins.insert_one(newDonor)
        res = db.prins.find({}, {"name"})
        for x in res:
            print(x)


def login(object):
    if object[0] != True:
        query = {"name": object[0], "password": object[1]}
        res = db.donorcol.find(query)
        for x in res:
            print(x)
    else:
        query = {"name": object[1], "password": object[2]}
        res = db.prins.find(query)
        print(res)
        for x in res:
            print(x)

# TOdo


def broadcastInfo(object):

    pass


def hashgenerator(object):
    traget = [str(i) for i in object]
    res = hashlib.sha256()
    for x in traget:
        res.update(x.encode("utf-8"))
    res = res.hexdigest()
    print(res)
    return res


def infoEncrypto(object):
    alist = ["name", "idNum", "phone"]
    key = object["password"]
    removePassword(object)
    for k in object:
        if k in alist:
            object[k] = cp.encrypt_oracle(key, str(object[k]))

    print(object)


def infoDecrypto(key, object):
    alist = ["name", "idNum", "phone"]
    for k in object:
        if k in alist:
            object[k] = cp.decrypt_oralce(key, str(object[k]))
    print(object)


def removePassword(object):
    del object["password"]
