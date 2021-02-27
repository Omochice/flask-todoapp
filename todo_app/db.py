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

    def insert(self, id: int, name: str) -> None:
        dt_now = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.todos.insert_one({
            "id": id,
            "title": name,
            "create_at": dt_now,
            "update_at": dt_now
        })

    def update(self, id: int) -> None:
        pass
