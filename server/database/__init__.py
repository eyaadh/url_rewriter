import pymongo
from server.common import Common


class DB:
    def __init__(self):
        self.db_client = pymongo.MongoClient(
            f"mongodb://"
            f"{Common().db_username}:{Common().db_password}@{Common().db_host}"
        )

        self.db = self.db_client[f"{Common().db_name}"]
