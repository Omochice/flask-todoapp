from flask_testing import TestCase
from todo_app.main import app
from todo_app.db import TodoAppDbClient


class BaseTestCase(TestCase):
    def create_app(self):
        app.config["DEBUG"] = True
        return app

    def setUp(self):
        self.app = self.app.test_client()

    def tearDown(self):
        client = TodoAppDbClient()
        client.delete_all()
