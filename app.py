# app.py
from flask import Flask, request, jsonify
import joblib
from flask_cors import CORS
import pandas as pd


app = Flask(__name__)
CORS(app)

# Charger le modèle
model = joblib.load('random_forest_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return jsonify({'prediction': int(prediction)})

if __name__ == '__main__':
    app.run(debug=True)
    
