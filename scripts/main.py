import os.path
import json
import urllib.request
from api import do_search

parking_data = do_search('Parking Violations Issued in')

print(parking_data)

## save response to data directory
with open(os.path.join('data', 'parking_data.json'), 'w') as file:
    json.dump(parking_data, file)

for key in parking_data.keys():
    url = parking_data[key]
    print(f'Fetching... {key}')
    file_name = key.replace(' ', '_')
    urllib.request.urlretrieve(url, f'data/{file_name}.csv')


