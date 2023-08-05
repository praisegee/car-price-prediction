import pickle

import numpy as np

# import sklearn
from flask import Flask, render_template, request

# from sklearn.preprocessing import StandardScaler

# instanciate flask object
app = Flask(__name__)
# load the trained model from pickle file
# model = pickle.load("models/gradient_model.pkl")


@app.route("/", methods=["GET"])
def home():
    return "Hello World"


if __name__ == "__main__":
    app.run(port=3000, debug=True)
