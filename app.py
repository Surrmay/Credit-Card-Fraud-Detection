# app.py - Simple Flask backend
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('fraud_detection_model.pkl')

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.json
    # Preprocess data to match your model's expected format
    features = preprocess_transaction(data)
    
    prediction = model.predict([features])[0]
    probability = model.predict_proba([features])[0][1]
    
    return jsonify({
        'fraudProbability': float(probability),
        'isFraud': bool(prediction),
        'riskLevel': 'HIGH' if probability > 0.7 else 'MEDIUM' if probability > 0.3 else 'LOW'
    })