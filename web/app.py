import os
from pathlib import Path

from flask import Flask, request, render_template

from langclass.models.predict_model import Predictor

current_file_path = Path(os.path.realpath(__file__))
vecparams_model_path = (
    current_file_path.parent.parent.parent / "models" / "vecparams_model.pkl"
)

predictor = Predictor(vecparams_model_path)

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def langclass_post():
    if request.method == "POST":
        code = request.form.get("code")
        return predictor.predict(code)
    return render_template("index.html", message="Hello Flask!")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
