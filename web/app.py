import os
from pathlib import Path

from flask import Flask, request, render_template
from waitress import serve

import sys

from langclass.models.predict_model import Predictor

current_file_path = Path(os.path.realpath(__file__))
vecparams_model_path = (
    current_file_path.parent.parent / "models" / "vecparams_model.pkl"
)

predictor = Predictor(vecparams_model_path)

app = Flask(__name__)

mode = "develop"
if len(sys.argv) > 1:
    mode = sys.argv[1]
if mode == "deploy":
    port = 80
else:
    port = 8080

@app.route("/", methods=["POST", "GET"])
def langclass_post():
    language = ""
    if request.method == "POST":
        code = request.form.get("code")
        language = predictor.predict(code)
    return render_template("index.html", language=language)


if __name__ == "__main__":
    if mode == "deploy":
        serve(app, port=port)
    else:
        app.run(debug=True, port=port)
