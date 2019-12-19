import pymongo

db_water = pymongo.MongoClient("mongodb://localhost:27017")["water"]
device_collection = db_water.device

# 获取 uuid 列表
ids = device_collection.distinct("uuid")
print("device id list:", ids)
