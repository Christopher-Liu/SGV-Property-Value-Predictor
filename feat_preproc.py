# Function for taking POST request form data and turning it into a 
# suitable form to pass into the predictor

# Large dictionary to "cache" values from health, ed, income indices and crime rate
city_indices = {'Hacienda Heights': {'HEALTH_IND': 7.62,
                                     'ED_INDEX': 5.77,
                                     'INCOME_IND': 5.88,
                                     'Rte_crim': 169.0},
                'La Puente': {'HEALTH_IND': 7.02,
                              'ED_INDEX': 2.76,
                              'INCOME_IND': 3.23,
                              'Rte_crim': 324.0},
                'Rowland Heights': {'HEALTH_IND': 8.77,
                                    'ED_INDEX': 5.55,
                                    'INCOME_IND': 4.46,
                                    'Rte_crim': 168.0},
                'West Covina': {'HEALTH_IND': 7.18,
                                'ED_INDEX': 4.96,
                                'INCOME_IND': 4.75,
                                'Rte_crim': 246.0},
                'Alhambra': {'HEALTH_IND': 7.38,
                             'ED_INDEX': 5.22,
                             'INCOME_IND': 4.66,
                             'Rte_crim': 168.0},
                'South Pasadena': {'HEALTH_IND': 8.01,
                                   'ED_INDEX': 8.71,
                                   'INCOME_IND': 8.08,
                                   'Rte_crim': 104.0},
                'Temple City': {'HEALTH_IND': 6.94,
                                'ED_INDEX': 6.34,
                                'INCOME_IND': 5.64,
                                'Rte_crim': 134.0},
                'San Gabriel': {'HEALTH_IND': 7.64,
                                'ED_INDEX': 5.31,
                                'INCOME_IND': 3.62,
                                'Rte_crim': 243.0},
                'Rosemead': {'HEALTH_IND': 7.43,
                             'ED_INDEX': 3.56,
                             'INCOME_IND': 2.75,
                             'Rte_crim': 303.0},
                'Monterey Park': {'HEALTH_IND': 7.96,
                                  'ED_INDEX': 5.02,
                                  'INCOME_IND': 4.58,
                                  'Rte_crim': 214.0},
                'South El Monte': {'HEALTH_IND': 8.18,
                                   'ED_INDEX': 2.07,
                                   'INCOME_IND': 2.2,
                                   'Rte_crim': 491.0878213712782},
                'El Monte': {'HEALTH_IND': 7.94,
                             'ED_INDEX': 2.65,
                             'INCOME_IND': 2.33,
                             'Rte_crim': 394.0},
                'Diamond Bar': {'HEALTH_IND': 8.08,
                                'ED_INDEX': 7.44,
                                'INCOME_IND': 6.62,
                                'Rte_crim': 116.0},
                'Walnut': {'HEALTH_IND': 8.24,
                           'ED_INDEX': 7.46,
                           'INCOME_IND': 6.87,
                           'Rte_crim': 83.0},
                'Pasadena': {'HEALTH_IND': 7.03,
                             'ED_INDEX': 6.83,
                             'INCOME_IND': 6.4,
                             'Rte_crim': 339.0},
                'Arcadia': {'HEALTH_IND': 8.03,
                            'ED_INDEX': 7.85,
                            'INCOME_IND': 6.63,
                            'Rte_crim': 146.0},
                'San Marino': {'HEALTH_IND': 8.56,
                               'ED_INDEX': 9.72,
                               'INCOME_IND': 10.0,
                               'Rte_crim': 141.89848582221282},
                'Sierra Madre': {'HEALTH_IND': 6.59,
                                 'ED_INDEX': 9.33,
                                 'INCOME_IND': 8.79,
                                 'Rte_crim': 261.8973456683808},
                'Monrovia': {'HEALTH_IND': 5.94,
                             'ED_INDEX': 6.11,
                             'INCOME_IND': 5.6,
                             'Rte_crim': 160.0},
                'Duarte': {'HEALTH_IND': 6.03,
                           'ED_INDEX': 5.44,
                           'INCOME_IND': 5.01,
                           'Rte_crim': 279.12038718355404},
                'Covina': {'HEALTH_IND': 6.15,
                           'ED_INDEX': 5.12,
                           'INCOME_IND': 4.93,
                           'Rte_crim': 334.0},
                'San Dimas': {'HEALTH_IND': 6.62,
                              'ED_INDEX': 6.65,
                              'INCOME_IND': 6.59,
                              'Rte_crim': 241.0},
                'Baldwin Park': {'HEALTH_IND': 6.92,
                                 'ED_INDEX': 3.08,
                                 'INCOME_IND': 2.72,
                                 'Rte_crim': 391.0},
                'Azusa': {'HEALTH_IND': 6.12,
                          'ED_INDEX': 4.6,
                          'INCOME_IND': 2.1,
                          'Rte_crim': 354.0},
                'Glendora': {'HEALTH_IND': 6.3,
                             'ED_INDEX': 6.0,
                             'INCOME_IND': 5.88,
                             'Rte_crim': 134.0},
                'Montebello': {'HEALTH_IND': 7.38,
                               'ED_INDEX': 3.7,
                               'INCOME_IND': 3.68,
                               'Rte_crim': 336.0},
                'Valinda': {'HEALTH_IND': 6.79,
                            'ED_INDEX': 2.95,
                            'INCOME_IND': 3.2,
                            'Rte_crim': 137.0},
                'Pico Rivera': {'HEALTH_IND': 6.37,
                                'ED_INDEX': 3.23,
                                'INCOME_IND': 3.71,
                                'Rte_crim': 343.0},
                'East Los Angeles': {'HEALTH_IND': 6.39,
                                     'ED_INDEX': 1.67,
                                     'INCOME_IND': 1.79,
                                     'Rte_crim': 480.0}}





def featurizer(data):
    processed_features = [float(data['Beds']), float(data['Baths']), float(data['Sq Feet'])]

    # Add in socioeconomic variables- uses the dictionary defined above
    processed_features.extend(list(city_indices[data['City']].values()))

    # Add in DTLA distance- this will be the average distance of all properties within each respective city

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