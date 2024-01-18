import requests
import json
from pprint import  pprint

res = requests.get('https://swapi.dev/api/people/3/')
text = res.text
data = json.loads(text)
data['name'] = 'Alexey'
print(data)

home_world_link = data['homeworld']
print(home_world_link)
res = requests.get(home_world_link)
pprint(res.text)

with open('swapi.log', 'w') as f_hand:
    json.dump(data, f_hand, indent=4)