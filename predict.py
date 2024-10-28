import pickle
import numpy as np

from flask import Flask, request, jsonify

def pred_single(client, dv, model):
    X = dv.transform(client)
    y_pred = model.predict_proba(X)[:,1]

    return y_pred[0]

model_file = 'model1.bin'
dv_file = 'dv.bin'

with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

with open(dv_file, 'rb') as f_in:
    dv = pickle.load(f_in)

app = Flask('subscription')

@app.route('/predict', methods = ['POST'])

def predict():
    client = request.get_json()

    prediction = pred_single(client, dv, model)
    subscription = prediction >= 0.5

    result = {
        'subscription_probability': float(prediction),
        'subscription': bool(subscription)
    }

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)

