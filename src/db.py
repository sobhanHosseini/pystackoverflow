import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client.stack_overflow_telegram_bot