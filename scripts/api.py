import json
import requests

url = 'https://opendata.arcgis.com/api/v3/search'

payload = {
    'q': 'Parking Violations Issued in',
    'catalog': {
        'groupIds': 'any(6664e0b92948483ab633b3080d466122)'
    }
}

headers = {
    'Content-Type': 'application/json'
}


def do_search():
    response = requests.request('POST', url, headers=headers, data=json.dumps(payload))
    response_data = {}
    return parse_search_response(response.json(), response_data)


def page_result(next_url, response_data):
    response = requests.request('GET', next_url)
    return parse_search_response(response.json(), response_data)


def parse_search_response(r, response_data):
    data = r['data']
    for d in data:
        print(d['attributes']['name'])
        if d['attributes']['name'].startswith('Parking Violations'):
            response_data[d['attributes']['name']] = d['links']['self']

    if 'next' in r['meta']:
        return page_result(r['meta']['next'], response_data)
    else:
        return response_data

parking_data = do_search()

print(parking_data)
