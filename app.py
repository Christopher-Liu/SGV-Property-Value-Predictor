from flask import Flask, render_template, request
import feat_preproc


# Static list of cities needed for populating the drop down menu
city_list = ['Alhambra', 'Arcadia', 'Azusa', 'Baldwin Park', 'Covina', 'Diamond Bar', 'Duarte', 
                'East Los Angeles', 'El Monte', 'Glendora', 'Hacienda Heights', 'La Puente', 'Monrovia',
                'Montebello', 'Monterey Park', 'Pasadena', 'Pico Rivera', 'Rosemead', 'Rowland Heights',
                'San Dimas', 'San Gabriel', 'San Marino', 'Sierra Madre', 'South El Monte',
                'South Pasadena', 'Temple City', 'Valinda', 'Walnut', 'West Covina']


app = Flask(__name__)

@app.route('/')
def home_page():


    return render_template('index.html', cities = city_list)


@app.route('/prediction', methods = ['POST'])
def prediction():

    # Need to take information from POST request and convert that
    # into features that the ML model can use. Then we render 
    # index.html with prediction results passed in as data.
    # Should define another function called featurizer that does
    # the processing of POST data into features. We've imported 
    # feat_preproc, so we can call: feat_preproc.featurizer()

    # return render_template('index.html', pred_output = 'Price: ${}'.format(pred_price))

    processed_features = feat_preproc.featurizer(request.form)



    # Whent this is finished, it should have
    # prediction = model.predict(processed_features)
    # return render_template('index.html', pred_vals = prediction, cities = city_list)

    return render_template('index.html', pred_vals = processed_features , cities = city_list)