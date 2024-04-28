import requests

api_key = '3c2c65f2-eb84-4f6e-a7ca-3b8d350cb6d6'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)