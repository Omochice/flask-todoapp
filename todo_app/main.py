from flask import Flask, request, jsonify, abort
from .db import TodoAppDbClient

app = Flask(__name__)
client = TodoAppDbClient()


@app.route("/", methods=["GET"])
def index():
    data = client.fetch_all()
    for d in data:
        del d["_id"]
    return jsonify(data)


@app.route("/", methods=["POST"])
def store_data():
    data = request.json
    err = client.insert({"title": data["title"], "id": data["id"]})
    response = jsonify()
    if err is not None:
        abort(409, err)
    return response, 200


@app.route("/<int:id>", methods=["GET"])
def show_one(id: int):
    data = client.fetch_one(id=id)
    if data is None:
        abort(404)
    del data["_id"]
    return jsonify(data)


@app.route("/", methods=["PUT"])
def update():
    client.update(request.json)
    return jsonify(), 200


@app.route("/", methods=["DELETE"])
def delete():
    res = client.delete(request.json)
    if res is not None:
        return abort(404, res)
    return jsonify(), 202


if __name__ == "__main__":
    app.run(debug=True)
