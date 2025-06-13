# 🏠 Boston House Price Prediction - Linear Regression with Flask

This project is part of the **Python Zero to Hero Bootcamp** and demonstrates how to train a **Linear Regression model** on the Boston Housing dataset and deploy it using **Flask**.

---

## 🚀 Project Overview

We trained a machine learning model to predict housing prices in Boston based on 13 features (like crime rate, number of rooms, etc.). This model is served using a Flask web application, where users can input features and get a predicted price.

---

## 📁 Repository Structure

boston-house-price-predictor/
├── app.py # Flask backend
├── boston_model.pkl # Trained machine learning model
├── boston_model.ipynb # Jupyter notebook used for training
├── templates/
│ └── index.html # Frontend HTML with custom CSS
└── README.md # Project documentation


---

## 🧠 Technologies Used

- Python
- Pandas, NumPy, Scikit-learn
- Jupyter Notebook
- Flask
- HTML & CSS

---

## 📊 Dataset

The model is trained on the **Boston Housing dataset**, which contains various features of neighborhoods in Boston and their median house prices.

> **Note**: This dataset is deprecated in newer versions of `scikit-learn`. If you're using a recent version, you can import it like this:

```python
from sklearn.datasets import fetch_openml
boston = fetch_openml(name="boston", version=1, as_frame=True)
