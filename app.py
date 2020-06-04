from flask import Flask, render_template, request
import feat_preproc


app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/prediction', methods = ['POST'])
def prediction():

    # Need to take information from POST request and convert that
    # into features that the ML model can use. Then we render 
    # index.html with prediction results passed in as data.
    # Should define another function called featurizer that does
    # the processing of POST data into features. We've imported 
    # feat_preproc, so we can call: feat_preproc.featurizer()

    # return render_template('index.html', pred_output = 'Price: ${}'.format(pred_price))

    return render_template('index.html', pred_val = request.form['first'] )