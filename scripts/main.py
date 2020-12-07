import os.path
import json
import urllib.request
from api import do_search

parking_data = []
config_path = os.path.join('data', 'config', 'parking_data.json')
if not os.path.exists(config_path):
    parking_data = do_search('Parking Violations Issued in')

    # save response to data directory
    with open(config_path, 'w') as file:
        json.dump(parking_data, file)
else:
    with open(config_path, 'r') as file:
        parking_data = json.load(file)

for key in parking_data.keys():
    url = parking_data[key]
    print(f'Fetching... {key}')
    file_name = key.replace(' ', '_')
    file_path = f'data/incoming/{file_name}.csv'
    # split date to get month and year
    # May 2018 -> ['May', '2018']
    date_parts = key.split(' ')
    if not os.path.exists(file_path) and date_parts[1] == '2018':
        urllib.request.urlretrieve(url, file_path)
