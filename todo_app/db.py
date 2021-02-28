from pymongo import MongoClient
from datetime import datetime
from typing import Optional


def get_now():
    return datetime.now().strftime("%Y-%m-%d %H:%M")


class TodoAppDbClient:
    def __init__(self) -> None:
        client = MongoClient()
        db = client.test
        db.authenticate(name="pymongo", password="pymongo")
        self.todos = db.todos

    def fetch_one(self, id: int) -> dict:
        return self.todos.find_one({"id": id})

    def fetch_all(self) -> list:
        return [d for d in self.todos.find()]

    def insert(self, query: dict) -> Optional[str]:
        dt_now = get_now()
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

    def delete(self, query: dict) -> Optional[str]:
        delete_result = self.todos.delete_one(query)
        if delete_result.deleted_count == 0:
            return "The request id is not exist"

    def delete_all(self):
        self.todos.delete_many({})

    def update(self, replace: dict) -> None:
        self.todos.update_one(
            {"id": replace["id"]},
            {"$set": {
                "title": replace["title"],
                "update_at": get_now()
            }})
