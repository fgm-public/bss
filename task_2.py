import requests

url = 'http://api.weatherbit.io/v2.0/current'

params = {
    'key': 'censored',
    'lang': 'ru',
    'city': 'Novosibirsk'
}

result = requests.get(url, params)

print(result.json())
