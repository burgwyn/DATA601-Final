import requests

url = 'https://opendata.arcgis.com/api/v3/search'

payload = "{" \
          "\"q\": \"Parking Violations in\"," \
          "\"catalog\":{\"groupIds\":\"any(d37febcec5094c719eb244d59d3ae08d,4c106214b9ba46aeb028a16134fa71cc,006f7f52404b4b4e85dea1e0938275f0,9f22ca286c814193bc0f87106df548fb,35d3981a82874e01b1c1df0aef7227c8,0fd6c262970c4442a66e57e3deb270d2,e5eae38d52fa46248918d57a91b511a0,73fa9cc1ce8e488b8c822c1c017887d6,685c2780f30644e3992194a454c2db50,586b466e82834506b1754a3b94bc5d3a,a7749d01300f4f87a8769d26a5df2181,489e982ea160416bb62a8247175ad9c0,5ff18aacf97f4008a277fa6c81cdb5df,ec224dd0c2294755a0e232d784eb1172,821474b35eb74c1b899f3b0f75e42ab8,b7d32c689e044f0997a1fbd5c9462249,fd8b3227eee74d509d93fa127b255fac,de7c93a55b084c8bb63140efe8475414,e4ea8f08ec834a53bd067676fc09274a,3cfdba546f1e40b0b430127c7cefd384,0204ece8c0344982a8923e43e93bbd13,499467eb06a546968283905708e7c05e,08cada661e7c41748df5a7042d3375d7,6664e0b92948483ab633b3080d466122,72c19e0ed89641ac83045a4597a6c9dc,6f754c5a004542bb9f1f8830258aa794,3d738aca3d274f6c8748256738e83f14,e24f6a47d94c493d99d6d99a8d77b3db,d3ad991e7c9447bf81c3ef4fac5f6696,696e1f4cb4f4464fa3ae72370f1d1eeb,95c59d84749742b7ad1e135c6e685009,0ef7f4b207e245b28b235a896be1c0f3,e60a958b3e8340b7ac3549ced5ec5157,42f1e95acd8845da8c7426a414aefb33,62be2f179f674941b393f1c9bc8ca73e,d9592387328c447c89fa07e8f4d5f2ff,e6c5e47b278342b9baf21632ea2f3b34,7e97b9f459934994a37300b2be196ba2,0d7907d5b2124e8681543aa61029430a,f3de8399eb0f493b84c8bbe076079ead,9f70eb9a4f2048b3920a476427467eea)\"," \
          "\"id\":\"any(39cd6202ee734299a675d3017ade87d5,d4b016cb36df404396340e9115d594a4,895e05ea980847dc9346d870c7b8359a,3d485be41bec4448a277cc4d9f2fd1ca,dfbd2546c70b4e84bbee9c8a8defcc70,378dcaff44ce4cd8aa52edfae596a6ed,69bf537cd3fc4f2b9231769695c6ff7c,1a277e421da84419a414d3bd20806413,f5ff9f233b10416fb5ef8c33b61abb06,39da6329c341484bb09dce08947d1692,98ffbfe3071749f6a18588713322c5bb,9b8d8720ba4047c9af0e7332b1f3b803,8c3b2972507443539ede792dd122e960,21fecd87381341bf93a2875a56b4e781,9e76411301584615aab3769f7d6bea21,6cf86b11649041cd9e5eee91ad4b62d5,06d7389b6e684e2a8cffac5bee97594d,16f78a1fbc5b4d9eb4f23379f89d0953,79d580a1022e40c6a53438bcc1de8da3,cabb5e1e6e144a968b4402a927318baf,0df25713b6454ab6b6edd19418636dd3,e3bd4394ad1d44fcb89fd5c335fe462c,6e21635d0b534a14b314d3c74816d563,0d132e17bafb42cf973042ef9b72ba91,5aaac85a1ab148d58fd026a38d287d38,5380fd34bf1d41e78a8730e2d0a997f3)\"}" \
          "}"
headers = {
    'Content-Type': 'application/json'
}


def do_search():
    response = requests.request('POST', url, headers=headers, data=payload)
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

# parking_data = do_search()

# print(parking_data)
