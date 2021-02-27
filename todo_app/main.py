from flask import Flask, request, jsonify, abort
from .db import TodoAppDbClient

app = Flask(__name__)
client = TodoAppDbClient()


@app.route("/")
def index():
    return "index page"


@app.route("/", methods=["POST"])
def store_data():
    data = request.json
    err = client.insert({"title": data["title"], "id": data["id"]})
    print(client.todos.find_one({"id": data["id"]}))
    response = jsonify()
    if err is not None:
        print([f for f in client.todos.find({})])
        abort(409, err)
    return response, 200


if __name__ == "__main__":
    app.run(debug=True)
