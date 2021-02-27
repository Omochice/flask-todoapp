from pymongo import MongoClient
from datetime import datetime
from typing import Optional


class TodoAppDbClient:
    def __init__(self) -> None:
        client = MongoClient()
        db = client.test
        db.authenticate(name="pymongo", password="pymongo")
        self.todos = db.todos

    def fetch_one(self, id: int) -> dict:
        return self.todos.find_one({"id": id})

    def fetch_all(self) -> list:
        return self.todos.find()

    def insert(self, query: dict) -> Optional[str]:
        dt_now = datetime.now().strftime("%Y-%m-%d %H:%M")
        rst = self.todos.find_one({"id": query["id"]})
        if rst is not None:
            return "The id exists already"
        # else:
        self.todos.insert_one({
            "id": query["id"],
            "title": query["title"],
            "create_at": dt_now,
            "update_at": dt_now
        })

    def remove(self):
        pass

    def remove_all(self):
        self.todos.delete_many({})
        # pass

    def update(self, id: int) -> None:
        pass
