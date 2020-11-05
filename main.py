import interfaces as it
import datastruct as ds


def register_test():
    candidate = ["jackson", "123123", 477856321459874563,
                 98745632145, True, "SE12", "se1"]
    it.register(candidate)


def login_test():
    data = [True, "1jackson", "123123"]
    it.login(data)


def hashgenerate_test():
    data = ["jackson", "123123", 477856321459874563,
            98745632145, True, "SE12", "se1"]
    it.hashgenerator(data)


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
        "name": "tom",
        # 证件类型
        "cType": ds.cType["type2"],
        "idNum": 478521456325896321,
        # 血型
        "bType": "O",
        "dType": ds.dType["type1"],
        # 献血量
        "bAmount": ds.bAmount[1],
        # 献血地址
        "saddress": ds.saddress["se1"],
        # 时间戳，系统生成，遵循下述格式
    }
    it.makeBloodInfo(infos)


def H_in_test():
    hos = "SE12"
    code = "67fc3cd4f49c469e0dee4083f0af33957e5d9d718f9bf32d44076577692ea5c9"
    it.Hospital.in_blood_info(hos, code)


def H_out_test():
    code = "167fc3cd4f49c469e0dee4083f0af33957e5d9d718f9bf32d44076577692ea5c9"
    it.Hospital.out_blood_info(code)


# H_in_test()
mBi_test()
