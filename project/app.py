import pickle
from xgboost import XGBClassifier
import pandas as pd
import numpy as np

from flask import Flask, render_template, request
app = Flask(__name__, static_folder='static')


with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    # Get the input data from the form

    input_names = ['profit on operating activities / financial expenses',
                   'net profit / sales',
                   'profit on sales / total assets',
                   'total assets / total liabilities',
                   'retained earnings / total assets'
                   ]

    if request.method == 'POST':

        inputs = np.array([])
        for name in input_names:
            input_value = request.form.get(name)
            if input_value is not None:
                input_data = float(input_value)
                inputs = np.append(inputs, input_data)
        data = {'profit on operating activities / financial expenses': [inputs[0]],
                'net profit / sales': [inputs[1]],
                'profit on sales / total assets': [inputs[2]],
                'total assets / total liabilities': [inputs[3]],
                'retained earnings / total assets': [inputs[4]]}
        print(data)
        print(inputs)
        df = pd.DataFrame(data)
        df.index = ['Row1']
    if len(inputs) == len(input_names):
        # Make the prediction if all input values were successfully collected
        prediction = model.predict(df)

        return f"Prediction: {prediction}"
        # Handle or return the prediction as needed
    else:
        print("len inputs: ")
        print(len(inputs))
        print("\n")
        print("len input_names: ")
        print(len(input_names))
        return f"Prediction: none"


if __name__ == "__main__":
    app.run(debug=True)
