import requests

url = "https://opendata.arcgis.com/api/v3/search?q=parking violations in"

payload={}
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
