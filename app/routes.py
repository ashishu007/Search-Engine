from app import flask_app
from flask import request, jsonify, render_template
from app.engine.rank import get_top_docs as gtp

@flask_app.route("/")
def hello():
    return render_template("default.html")

@flask_app.route("/res", methods=["GET", "POST"])
def res():
    # query = request.args.get('q')
    # algo = request.args.get('a')
    # corpus = request.args.get('c')

    if request.method == 'POST':
        form_result = request.form
        form_r = form_result.to_dict(flat=False)
    print("form_r", form_r)

    res = gtp(form_r["query"][0], form_r["algo"][0], form_r["corpus"][0])
    return jsonify(res)

if __name__ == "__main__":
    flask_app.run()