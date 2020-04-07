import requests
import json

query = 'kill'
page_size = '10'
apiKey = 'api_key'
from_date = '2020-01-01'
to_date = '2020-01-31'

url = "https://content.guardianapis.com/search?q=" + query + "&show-blocks=all&from-date=" + from_date + "&api-key=" + apiKey + "&page-size=" + page_size + "&to-date=" + to_date

r = requests.get(url)
results = r.json()['response']['results']

f = open(query + ".json", "w")
f.write('[')

data = {}
data['news'] = {}

i = 0
while i < int(page_size):
    data['news'].update({
        'date': r.json()['response']['results'][i]['webPublicationDate'],
        'body': r.json()['response']['results'][i]['blocks']['body'][0]['bodyHtml']
    })

    jsonVal = json.dumps(data['news'])
    print(jsonVal)

    if int(page_size) - 1 == i:
        f.write(jsonVal)
        break
    else:
        f.write(jsonVal + ',')
        i += 1

f.write(']')
f.close()
