import json
import requests as req

payload = {
    'catalog': {
        'groupIds': 'any(6664e0b92948483ab633b3080d466122)'
    }
}

headers = {
    'Content-Type': 'application/json'
}


def do_search(q, url='https://opendata.arcgis.com/api/v3/search'):
    payload['q'] = q
    payload_json = json.dumps(payload)
    response = req.request('POST', url, headers=headers, data=payload_json)
    response_data = {}
    return parse_search_response(response.json(), response_data)


def page_result(next_url, response_data):
    response = req.request('GET', next_url)
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


def format_csv_url(url):
    # convert
    # https://opendata.arcgis.com/api/v3/datasets/7e688a52e65d49c0beef48289860f465_0
    # to
    # https://opendata.arcgis.com/datasets/ef6a77dd0bf6448ca8a8cb15f114b15e_7.csv
    csv_url = url.replace('/api/v3', '')
    return csv_url + '.csv'
