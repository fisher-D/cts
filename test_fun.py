import interfaces as it
import datastruct as ds

names = "张三"
idNumm = "123456789987654321"
phone = "12345678987"


def register_test():
    candidate = [names, "a1234567", idNumm,
                 phone, False, "SE12", "se1"]
    it.register(candidate)


def login_test():
    data = [True, "1jackson", "123123"]
    it.login(data)


def hashgenerate_test():
    data = ["jackson1", "123123", "477856321459874563",
            "98745632145", "True", "SE12", "se1"]
    return it.hashgenerator(data)


def infoEn_test():
    data = {"name": "jackson",
            "password": "123123",
            "idNum": 477856321459874563,
            "phone": 98745632145,
            "principals": True,
            "chospital": "SE12",
            "saddress": "se1"}
    it.infoEncrypto(data)


def infoDe_test():
    key = "123123"
    data = {'name': 'ea/LA87PkSlV6xsNJWSJ6g==',
            'idNum': 'fgl6h8B1T8px3g94NQMEaaL+mA9d5cewCcfFNh3gRpA=',
            'phone': 'VVtDbp1Gn/q2rv13TwWd+w==',
            'principals': True, 'chospital': 'SE12', 'saddress': 'se1'}
    it.infoDecrypto(key, data)


def mBi_test():
    infos = {
        # 初始没有，由hashgenerator产生
        "bHashCode": "",
        "name": names,
        # 证件类型
        "cType": ds.cType["type2"],
        "idNum": idNumm,
        # 血型
        "bType": "AB",
        "dType": ds.dType["type1"],
        # 献血量
        "bAmount": ds.bAmount[1],
        # 献血地址
        "saddress": ds.saddress["se1"],
        # 时间戳，系统生成，遵循下述格式
    }
    return it.makeBloodInfo(infos)


def H_in_test(res):
    hos = "SW"
    code = res
    it.Hospital.in_blood_info(hos, code)


def H_out_test():
    code = "2dd059331008bad15cbe38e5a19c0f7ec549ac67c22d52432cf37c5ce10d450c"
    it.Hospital.out_blood_info(code)


def mC_test(res):
    Hospital = "SW"
    code = res
    it.Hospital.makeCerti(Hospital, code)


# 注册用户
register_test()
# 假设用户去献血
# 工作人员为其生成血液信息
# res 为该信息的hash值
res = mBi_test()

# 这里为医院的功能
# 使用血液信息
# 在医院验证血液信息后
# 上传入库信息进入区块链
H_in_test(res)

# 这里为用户生成献血证书
# 并上链
mC_test(res)
