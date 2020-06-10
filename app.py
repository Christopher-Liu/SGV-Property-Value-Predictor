from flask import Flask, render_template, request
import feat_preproc
import pickle
import numpy as np


# Load serialized predictor model (pickle file)
prop_model = pickle.load(open('prop_model.pkl', 'rb'))


# Static list of cities needed for populating the drop down menu
city_list = ['Alhambra', 'Arcadia', 'Azusa', 'Baldwin Park', 'Covina', 'Diamond Bar', 'Duarte', 
                'East Los Angeles', 'El Monte', 'Glendora', 'Hacienda Heights', 'La Puente', 'Monrovia',
                'Montebello', 'Monterey Park', 'Pasadena', 'Pico Rivera', 'Rosemead', 'Rowland Heights',
                'San Dimas', 'San Gabriel', 'San Marino', 'Sierra Madre', 'South El Monte',
                'South Pasadena', 'Temple City', 'Valinda', 'Walnut', 'West Covina']

# Static list of all 6 property types for populating drop down menu
property_types = ['Single Family Residential', 'Condo/Co-op', 'Townhouse', 'Multi-Family (2-4 Unit)', 
                  'Mobile/Manufactured Home', 'Multi-Family (5+ Unit)']



app = Flask(__name__)

@app.route('/')
def home_page():

    return render_template('index.html', cities = city_list, prop_type = property_types)


@app.route('/prediction', methods = ['POST'])
def prediction():
    processed_features = feat_preproc.featurizer(request.form)

    prediction = prop_model.predict(np.array(processed_features).reshape(1, -1))

    return render_template('index.html', pred_vals = 'Estimated Property Value: ${}'.format(int(prediction)), cities = city_list, prop_type = property_types)


if __name__ == "__main__":
    app.run(debug=True)