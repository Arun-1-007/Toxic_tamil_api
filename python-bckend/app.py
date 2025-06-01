from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('python-bckend/best_model.pkl')
vectorizer = joblib.load('python-bckend/tfidf_vectorizer .pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['comment']
    features = vectorizer.transform([data])
    prediction = model.predict(features)[0]
    confidence = model.predict_proba(features)[0][1] if hasattr(model, 'predict_proba') else 0.5
    return jsonify({'label': 'toxic' if prediction == 1 else 'non-toxic', 'confidence': float(confidence)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
