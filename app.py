# app.py
from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('boston_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(request.form.get(f)) for f in request.form]
    final_input = np.array([features])
    prediction = model.predict(final_input)[0]
    return render_template('index.html', prediction_text=f'Estimated House Price: ${prediction*1000:.2f}')

if __name__ == '__main__':
    app.run(debug=True)

