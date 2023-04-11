from flask import Flask, request
import db_helper
import post
import json

db = db_helper
app = Flask(__name__)


@app.route("/views/posts", methods=["POST", "GET"])
def views_post():
    request_message = request.query_string
    print(request_message)

    value = db.select_post()
    return value


@app.route("/post/upload", methods=["POST", "GET"])
def upload_post():
    request_message = request.query_string
    print(request_message)

    _post = post.Post(0, 'abcd', 'as', '2023-05-05 11:11:11', '2023-05-05 11:11:11', 0, 0, 0, 0, 0)

    db.insert_post(_post)

    return 'ok'


@app.route("/post/delete", methods=["POST", "GET"])
def delete_post():
    request_message = request.query_string
    print(request_message)

    _post = post.Post(0, 'abcd', 'as', '2023-05-05 11:11:11', '2023-05-05 11:11:11', 0, 0, 0, 0, 0)

    db.insert_post(_post)

    return 'ok'


def run():
    app.run(host="0.0.0.0", port=443, debug=True)
