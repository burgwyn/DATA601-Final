import json
import unittest
import responses

from scripts import api

mock_response = {
    "data":
        [
            {
                "attributes": {"name": "Parking Violations in January 2000"},
                "links": {"self": "http://localhost/self"},
            }
        ],
    "meta": {"link": "http://localhost/next"}
}

mock_response_data = {
    "Parking Violations in January 2000": "http://localhost/self"
}


class TestApiMethods(unittest.TestCase):

    @responses.activate
    def test_so_search(self):
        responses.add(responses.POST,
                      "https://opendata.arcgis.com/api/v3/search",
                      body=json.dumps(mock_response),
                      content_type="application/json")

        assert api.do_search('Test search') == mock_response_data

    @responses.activate
    def test_page_results(self):
        responses.add(responses.GET,
                      "http://localhost/next",
                      body=json.dumps(mock_response),
                      content_type="application/json")

        assert api.page_result("http://localhost/next",
                               {}) == mock_response_data

    def test_parse_search_response(self):
        assert api.parse_search_response(mock_response,
                                         {}) == mock_response_data

    def test_format_csv_url(self):
        assert api.format_csv_url('https://opendata.arcgis.com/api/v3/datasets/f3e9e7239fb54f19919a718307eefbbe_9') ==\
               'https://opendata.arcgis.com/datasets/f3e9e7239fb54f19919a718307eefbbe_9.csv'


if __name__ == '__main__':
    unittest.main()
