import numpy as np
import pandas as pd
import requests
from YelpAPIConfig import get_my_key


API_KEY = get_my_key
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' %API_KEY}

# Define the parameters
PARAMETERS = {
    'term':'restaurant',
    'limit':50,
    'location':'Boston',
    'radius': 10000
}


print('Getting New Data...')
# Make a request to the yelp API
response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)

# convert JSON String to Dictionary
business_data = response.json()
for biz in business_data['businesses']:
    print(biz['name'])

