from flask import Flask, request, jsonify # type: ignore
import joblib
import numpy as np

model = joblib.load('Models/RandomForestRegressor.joblib')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    features = np.array([[
        data['brand'],
        data['battery_capacity_(mah)'],
        data['screen_size_(inches)'],
        data['resolution_x'],
        data['resolution_y'],
        data['processor'],
        data['RAM_(MB)'],
        data['internal_storage_(GB)'],
        data['rear_camera'],
        data['front_camera'],
        data['OS'],
        data['number_of_sims']
    ]])

    prediction = model.predict(features)

    return jsonify({'predicted_price': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
