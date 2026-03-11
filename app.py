from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

app = Flask(__name__)
CORS(app)

# Load and preprocess data
df = pd.read_csv("anemia.csv")
df.rename(columns={'Gender': 'gender', 'Hemoglobin': 'hemoglobin',
                   'MCH': 'mch', 'MCHC': 'mchc', 'MCV': 'mcv',
                   'Result': 'target'}, inplace=True)

X = df[['gender', 'hemoglobin', 'mch', 'mchc', 'mcv']]
y = df['target']

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(x_train, y_train)

print("Model Accuracy:", accuracy_score(y_test, model.predict(x_test)))

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        input_values = [float(data[feature]) for feature in ['gender', 'hemoglobin', 'mch', 'mchc', 'mcv']]
        sample = pd.DataFrame([input_values], columns=['gender', 'hemoglobin', 'mch', 'mchc', 'mcv'])

        prediction = model.predict(sample)[0]
        result = "You don't have any Anemic Disease" if prediction == 0 else "You have Anemic Disease"

        return jsonify({ "result": result })

    except Exception as e:
        print("🔥 ERROR:", e)
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
