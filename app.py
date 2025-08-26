from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import pickle
import os

app = Flask(__name__)

# Load model once at startup
MODEL_PATH = os.path.join("model", "model.pkl")
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# Map numeric prediction -> class name
IRIS_LABELS = {0: "setosa", 1: "versicolor", 2: "virginica"}

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Read form values in the expected order
        sepal_length = float(request.form.get("sepal_length"))
        sepal_width  = float(request.form.get("sepal_width"))
        petal_length = float(request.form.get("petal_length"))
        petal_width  = float(request.form.get("petal_width"))

        features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        y_pred = model.predict(features)[0]
        label = IRIS_LABELS.get(int(y_pred), str(y_pred))

        # Optional: confidence using predict_proba (if available)
        try:
            proba = model.predict_proba(features).max()
            confidence = round(float(proba) * 100, 2)
        except Exception:
            confidence = None

        return render_template(
            "result.html",
            label=label,
            confidence=confidence,
            inputs={
                "sepal_length": sepal_length,
                "sepal_width": sepal_width,
                "petal_length": petal_length,
                "petal_width": petal_width,
            },
        )
    except Exception as e:
        # Fallback: redirect back with a simple error message (kept minimal)
        return render_template("index.html", error=str(e))

if __name__ == "__main__":
    # For local development
    app.run(debug=True)
