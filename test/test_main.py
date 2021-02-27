from base import BaseTestCase
import pytest
import json


class TestTodoAPI(BaseTestCase):
    def test_get_index(self):
        response = self.app.get("/")
        self.assert_200(response)

    def test_post_todo(self):
        post_param = {"title": "go to school", "id": 1}
        response = self.app.post("/",
                                 data=json.dumps(post_param),
                                 content_type="application/json")
        self.assert_status(response, 200)

    def test_post_some_query(self):
        post_param = {"title": "go to school", "id": 1}    # same one
        response = self.app.post("/",
                                 data=json.dumps(post_param),
                                 content_type="application/json")
        self.assert_status(response, 409)
