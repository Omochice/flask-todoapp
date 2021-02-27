from base import BaseTestCase
import pytest
import json


class TestTodoAPI(BaseTestCase):
    def test_get_index(self):
        response = self.app.get("/")
        self.assert_200(response)

    def test_post_todo(self):
        post_param = "go to school"

        response = self.app.post("/", data=post_param, content_type="text")
        self.assert_status(response, 200)
