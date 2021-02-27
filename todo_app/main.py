from flask import Flask, request, jsonify
from .db import TodoAppDbClient

app = Flask(__name__)
client = TodoAppDbClient()


@app.route("/")
def index():
    return "index page"


@app.route("/", methods=["POST"])
def store_data():
    data = request.json
    client.insert({"title": data["title"], "id": data["id"]})
    response = jsonify()
    return response, 200


if __name__ == "__main__":
    app.run(debug=True)
