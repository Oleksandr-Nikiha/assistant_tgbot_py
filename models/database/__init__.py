from app import config

from . import userDB
from . import accountDB

user_db = userDB.UserMongoDB(username=config.MONGO_USER, password=config.MONGO_PASSWORD, url=config.MONGO_URL)
acc_db = accountDB.AccountingDB(username=config.MONGO_USER, password=config.MONGO_PASSWORD, url=config.MONGO_URL)