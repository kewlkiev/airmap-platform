# Code for platform verification


import requests

params = (
    ('geometry', '{"type":"Polygon","coordinates":[[[-118.6578369140625,34.11180455556899],[-118.43261718749999,33.694637550483186],[-117.97393798828125,33.62376800118811],[-117.88330078125,33.80197351806589],[-118.6578369140625,34.11180455556899]]]}'),
    ('types', 'airport,controlled_airspace,tfr,wildfire'),
    ('full', 'true'),
    ('geometry_format', 'wkt'),
)


authHeaders = {"X-API-Key":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjcmVkZW50aWFsX2lkIjoiY3JlZGVudGlhbHw0UEtQUktBU1phcFBXSkZZYUxLMEdUeDlxZW5QIiwiYXBwbGljYXRpb25faWQiOiJhcHBsaWNhdGlvbnwzTEJFNG9PdUJ2NjJKV1M0T2JMUFBDbm1RUHFiIiwib3JnYW5pemF0aW9uX2lkIjoiZGV2ZWxvcGVyfHlFWjl3RzVGMjgwTEdkQzlnUUpNUUYwRHY4bjciLCJpYXQiOjE1Mzc3MDg0NzZ9.4dy_syMAMs-1oQT5vyq7s3a20drbnbJ6WvUTtMK0PHg"}

import json,pprint
response = requests.get('https://api.airmap.com/airspace/v2/search', params=params , headers=authHeaders)


response = requests.get('https://api.airmap.com/aircraft/v2/manufacturer',headers = authHeaders)



responseDict= json.loads(response.text)
print type(response.text)
print(responseDict)
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://api.airmap.com/airspace/v2/search?geometry=%7B%22type%22:%22Polygon%22,%22coordinates%22:%5B%5B%5B-118.6578369140625,34.11180455556899%5D,%5B-118.43261718749999,33.694637550483186%5D,%5B-117.97393798828125,33.62376800118811%5D,%5B-117.88330078125,33.80197351806589%5D,%5B-118.6578369140625,34.11180455556899%5D%5D%5D%7D&types=airport,controlled_airspace,tfr,wildfire&full=true&geometry_format=wkt')

