import json
from api import do_search

parking_data = do_search('Parking Violations Issued in')

print(parking_data)

