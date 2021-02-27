from base import BaseTestCase
import pytest
import json


class TestTodoAPI(BaseTestCase):
    def post_one(self, title, id):
        post_item = {"title": title, "id": id}
        return self.app.post("/",
                             data=json.dumps(post_item),
                             content_type="application/json")

    def test_get_index(self):
        response = self.app.get("/")
        self.assert_200(response)

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
        res = self.post_one("foo", focus_id)
        res = self.app.get(f"/{focus_id}")
        print(res)
        self.assert_equal(False == True)
