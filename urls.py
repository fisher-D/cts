from wutongchain_cts.api import CTSAPI
app_id = "30a3531c-1ce7-11eb-8a37-fa163ec0b2f0"
secret_key = "30a61456-1ce7-11eb-8a37-fa163ec0b2f0"
cts_instance = CTSAPI(app_id, secret_key)


def get_height():
    height = cts_instance.get_height().json()["data"]["height"]
    return height


def get_block_info(height):
    block_info = cts_instance.get_block_detail_by_height(height).json()
    return block_info


def post_info(data, ids):
    data = 'test/' + str(data) + '_by_wally'
    business_id = str(ids)
    print(cts_instance.put_data(data=data, business_id=business_id).json())


# data = {"name": "jackson",
#         "password": "123123",
#         "idNum": 477856321459874563,
#         "phone": 98745632145,
#         "principals": True,
#         "chospital": "SE12",
#         "saddress": "se1"}
# ids = "bigdata_test"
# post_info(data, ids)
print(get_block_info(get_height()-1))
