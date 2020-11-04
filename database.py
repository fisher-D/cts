import pymongo

hosts = "192.168.3.2"


def __init__():
    myclient = pymongo.MongoClient("mongodb://"+hosts+":27017")
    return myclient["cts"]


mydb = __init__()
donorcol = mydb["donor"]
hospitalcoll = mydb["hospital"]
stationcoll = mydb["station"]
cert_coll = mydb["certifi"]
blood_info = mydb["blood"]
in_infos = mydb["in_info"]
out_infos = mydb["out_info"]
prins = mydb["principals"]
