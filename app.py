import json
import pickle
import numpy as np
from lib import feat_preproc
from flask import Flask, render_template, request


# Load serialized predictor model (pickle file)
prop_model = pickle.load(open('./models/rf_model.pkl', 'rb'))


# Load JSON file containing socioeconomic data need for making predictions
with open('./static/data/city_socioeconomic_indices.json','r') as city_dat:
    city_socioeconomic_indices = json.load(city_dat)

# Load txt file containing list of cities needed for populating the drop down menu
with open('./static/data/city_names.txt', 'r') as city_dat:
    city_names = city_dat.read().splitlines()

# Load txt file containing list of all property types for populating drop down menu
with open('./static/data/property_types.txt', 'r') as prop_dat:
    property_types = prop_dat.read().splitlines()




app = Flask(__name__)

@app.route('/')
def home_page():

    return render_template('index.html', cities = city_names, prop_type = property_types)


@app.route('/prediction', methods = ['POST'])
def prediction():
    processed_features = feat_preproc.featurizer(request.form, city_socioeconomic_indices)

    prediction = prop_model.predict(np.array(processed_features).reshape(1, -1))

    return render_template('index.html', pred_vals = 'Estimated Property Value: ${}'.format(int(prediction)), cities = city_names, prop_type = property_types)


if __name__ == "__main__":
    app.run()