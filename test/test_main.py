from base import BaseTestCase
import pytest
import json


class TestTodoAPI(BaseTestCase):
    def post_one(self, title, id):
        post_item = {"title": title, "id": id}
        return self.app.post("/",
                             data=json.dumps(post_item),
                             content_type="application/json")

    def test_post_todo(self):
        response = self.post_one("test post", 1)
        self.assert_status(response, 200)

    def test_post_some_query(self):
        res = self.post_one("this will be stored", 1)
        self.assert_status(res, 200)

        res = self.post_one("this will be rejected", 1)
        self.assert_status(res, 409)

        res = self.post_one("this will be stored", 2)
        self.assert_status(res, 200)

    def test_show_one(self):
        focus_id = 1
        _ = self.post_one("foo", focus_id)
        res = self.app.get(f"/{focus_id}")
        assert (res.is_json)

    def test_show_all(self):
        res = self.app.get("/")
        assert (type(res.json) == list)
        _ = self.post_one("one", 1)
        _ = self.post_one("two", 2)
        res = self.app.get(f"/")
        self.assert_status(res, 200)
        assert (len(res.json) == 2)

    def test_update(self):
        _ = self.post_one("old name", 1)
        new_title = "new name"
        res = self.app.put("/",
                           data=json.dumps({
                               "title": new_title,
                               "id": 1
                           }),
                           content_type="application/json")
        self.assert_status(res, 200)
        res = self.app.get("/1")
        assert (res.json["title"] == new_title)
