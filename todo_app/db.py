from pymongo import MongoClient
from datetime import datetime


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

    def insert(self, query: dict) -> None:
        dt_now = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.todos.insert_one({
            "id": query["id"],
            "title": query["title"],
            "create_at": dt_now,
            "update_at": dt_now
        })

    def update(self, id: int) -> None:
        pass
