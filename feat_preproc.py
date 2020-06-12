# Function for taking POST request form data and turning it into a 
# suitable form to pass into the predictor


def featurizer(data, socioeconomic_data):
    processed_features = [float(data['Beds']), float(data['Baths']), float(data['Sq Feet'])]

    # Add in socioeconomic variables and average DTLA distance- uses the dictionary defined above
    processed_features.extend(list(socioeconomic_data[data['City']].values()))

    # The order of the dummy variable columns for the model is: [NW, SE, SW]
    # If the selected city is in NE, then we simply add [0, 0, 0]
    if data['City'] in ['Alhambra', 'San Gabriel', 'Rosemead', 'Monterey Park', 'South El Monte', 'El Monte', 'Montebello', 'Pico Rivera', 'East Los Angeles']:
        processed_features.extend([0, 0, 1]) # 'SW'
    elif data['City'] in ['South Pasadena', 'Temple City', 'Pasadena', 'Arcadia', 'San Marino', 'Sierra Madre', 'Monrovia', 'Duarte']:
        processed_features.extend([1, 0, 0])  # 'NW
    elif data['City'] in ['Hacienda Heights', 'La Puente', 'Rowland Heights', 'Diamond Bar', 'Walnut', 'Valinda']:
        processed_features.extend([0, 1, 0])  # 'SE'
    else:
        processed_features.extend([0, 0, 0])  # 'NE'


    # Add in dummy variable columns for the property type
    if data['Prop_Type'] == 'Mobile/Manufactured Home':
        processed_features.extend([1, 0, 0, 0, 0])
    elif data['Prop_Type'] == 'Multi-Family (2-4 Unit)':
        processed_features.extend([0, 1, 0, 0, 0])
    elif data['Prop_Type'] == 'Multi-Family (5+ Unit)':
        processed_features.extend([0, 0, 1, 0, 0])
    elif data['Prop_Type'] == 'Single Family Residential':
        processed_features.extend([0, 0, 0, 1, 0])
    elif data['Prop_Type'] == 'Townhouse':
        processed_features.extend([0, 0, 0, 0, 1])
    else: # 'Condo/Co-op'
        processed_features.extend([0, 0, 0, 0, 0])


    return processed_features