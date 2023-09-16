# Importing module for Flask app
from flask import Flask, render_template, request
import pickle

# Create a Flask app
application = Flask(__name__)

model = pickle.load(open('model_pickle', 'rb'))

# Create a route for the home page
@application.route('/')
def index():
    return render_template('index.html')

# Create a route for handling the prediction
@application.route('/predict', methods=['POST'])
def predict():
    area = int(request.form['area'])
    #bedrooms = int(request.form['bedrooms'])

    prediction = model.predict([[area]])

    return render_template('index.html',prediction =prediction)
  # Return the numerical prediction value as a string

if __name__ == '__main__':
    application.run(debug=True)
