import os
import pickle
from flask import Flask, jsonify, render_template, request
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load trained model and scaler
model_path = "model/model.pkl"
scaler_path = "model/scaler.pkl"

with open(model_path, "rb") as f:
  model = pickle.load(f)

with open(scaler_path, "rb") as f:
  scaler = pickle.load(f)


@app.route("/")
def home():
  return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
  try:
    data = request.get_json()

    # Extract values from JS request
    hours_studied = float(data["hours_studied"])
    attendance = float(data["attendance"])
    previous_scores = float(data["previous_scores"])
    sleep_hours = float(data["sleep_hours"])
    extracurricular = int(data["extracurricular"])

    # Create DataFrame
    input_data = pd.DataFrame({
        "Hours_Studied": [hours_studied],
        "Attendance": [attendance],
        "Previous_Scores": [previous_scores],
        "Sleep_Hours": [sleep_hours],
        "Extracurricular_Activities": [extracurricular],
    })

    # Scale and predict
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]
    prediction = float(np.clip(prediction, 0, 100))

    # Category determination
    if prediction >= 85:
      category = "Excellent 🌟"
    elif prediction >= 70:
      category = "Good 👍"
    elif prediction >= 50:
      category = "Average / Needs Improvement ⚠️"
    else:
      category = "At Risk 🚨"

    return jsonify({
        "status": "success",
        "score": round(prediction, 2),
        "category": category,
    })

  except Exception as e:
    return jsonify({"status": "error", "message": str(e)}), 400


if __name__ == "__main__":
  app.run(debug=True, port=5000)