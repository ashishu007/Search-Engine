from app import flask_app
from flask import request, jsonify
from app.engine.rank import get_top_docs as gtp

@flask_app.route("/")
def hello():
    n = "Ashish"
    return jsonify({"msg": f"hello {n}"})

@flask_app.route("/res")
def res():
    query = request.args.get('q')
    algo = request.args.get('a')
    corpus = request.args.get('c')
    res = gtp(query, algo, corpus)
    return jsonify(res)

if __name__ == "__main__":
    flask_app.run()