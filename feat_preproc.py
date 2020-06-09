# Function for taking POST request form data and turning it into a 
# suitable form to pass into the predictor

def featurizer(data):
    processed_features = [float(data['Beds']), float(data['Baths']), float(data['Sq Feet'])]




    # The order of the dummy variable columns for the model is: [NW, SE, SW]
    # If the selected city is in NE, then we simply return [0, 0, 0]
    if data['City'] in ['Alhambra', 'San Gabriel', 'Rosemead', 'Monterey Park', 'South El Monte', 'El Monte', 'Montebello', 'Pico Rivera', 'East Los Angeles']:
        processed_features.extend([0, 0, 1]) # 'SW'
    elif data['City'] in ['South Pasadena', 'Temple City', 'Pasadena', 'Arcadia', 'San Marino', 'Sierra Madre', 'Monrovia', 'Duarte']:
        processed_features.extend([1, 0, 0])  # 'NW
    elif data['City'] in ['Hacienda Heights', 'La Puente', 'Rowland Heights', 'Diamond Bar', 'Walnut', 'Valinda']:
        processed_features.extend([0, 1, 0])  # 'SE'
    else:
        processed_features.extend([0, 0, 0])  # 'NE'

    return processed_features