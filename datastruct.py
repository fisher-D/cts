# Certification Type
# 证件类型
cType = {
    "type1": "护照",
    "type2": "居民身份证"
}

# 献血类型
dType = {
    "type1": "半血",
    "type2": "全血"
}
# 献血量
bAmount = [200, 400]

# 献血站地址
saddress = {
    "g1": "广州花园第一献血站",
    "g12": "天河区第一街道第二献血站",
    "y1": "河南省郑州市第一献血站",
    "se1": "苏州观前街献血站"
}

# 发证单位，医院
chospital = {
    "G1": "广东省第一人民医院",
    "SE12": "江苏省苏州市九龙医院",
    "SW": "苏州西医院"
}

# 献血者注册信息
# principal 为特殊字段
# 普通用户不具有该字段
# 仅当该用户为操作人角色时
# 由后端人员在系统添加字段与内容


Donor = {
    "name": "jack",
    "password": "aa123",
    "idNum": 478521456325896321,
    "phone": 14789693145
    # "principal":True,
    # "chospital":chospital["SE12"],
    # "saddress":saddress["se1"]
}
# a,b,c 是特殊的Donor
# 由makePrincipal()方法产生
# 具有principl,chospital和saddress 字段
# 且字段值不能为空
# 使用copy仅为展示
a = Donor.copy()
b = Donor.copy()
c = Donor.copy()

# 操作员序列
Principals = [a, b, c]

# 献血站注册信息
Station = {
    "sadress": saddress["se1"],
    "chospital": chospital["SE12"],
    # 系统操作人
    "principal": Principals[1]
}

Hospital = {
    "Code": "SE12",
    "location": "江苏省苏州市九龙医院",
    "principl": Principals[2]
}
# 血液信息
BloodInfo = {
    # 初始没有，由hashgenerator产生
    "bHashCode": "YH8827180348269ZI",
    "name": "jack",
    # 证件类型
    "cType": cType["type2"],
    "idNum": 478521456325896321,
    # 血型
    "bType": "O",
    "dType": dType["type1"],
    # 献血量
    "bAmount": bAmount[1],
    # 献血地址
    "saddress": saddress["se1"],
    # 时间戳，系统生成，遵循下述格式
    "timeStamp": "2020-11-19 11:32:16"
}

Certification = {
    # 献血编号，同时也是该证书的hash
    "cHashcode": "CZ118276517268ER",
    "inHashCode": "ZH778301749E7U29",
    "BloodInfo": BloodInfo,
    # 入库医院
    "chospital": chospital["SE12"],
    # 时间戳，系统生成，遵循下述格式
    "timeStamp": "2020-11-21 15:32:16"
}

In_Info = {
    "inHashCode": "ZH778301749E7U29",
    "bHashCode": "YH8827180348269ZI",
    "chosptial": chospital["SE12"],
    "timeStamp": "2020-11-21 15:32:16"
}

Out_Info = {
    "outHashCode": "JJ82739193840401",
    "inHashCode": "ZH778301749E7U29",
    "bHashCode": "YH8827180348269ZI",
    "timeStamp": "2020-11-21 15:32:16"
}
