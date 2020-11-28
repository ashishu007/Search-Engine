from app import app
from flask import request, jsonify, render_template
from app.engine.rank import get_top_docs as gtp

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/result", methods=["GET", "POST"])
def result():
    # query = request.args.get('q')
    # algo = request.args.get('a')
    # corpus = request.args.get('c')

    if request.method == 'POST':
        form_result = request.form
        form_r = form_result.to_dict(flat=False)
    print("form_r", form_r)

    res = gtp(form_r["query"][0], form_r["algo"][0], "abstracts")
    return render_template("result.html", docs=res, query=form_r["query"][0], num_docs=len(res))

if __name__ == "__main__":
    app.run()
    # flask_app.run(host='0.0.0.0')