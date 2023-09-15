import requests
import json

token = '64f837cb7a7dc64f837cb7a7de'

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}
data = {
    "token": token,
}

def news():
    response = requests.get('https://datsorange.devteam.games/news/LatestNews5Minutes', headers=headers)
    response = response.json()
    print(response[0]['date'])
    print(response[0]['text'])
    print(response[0]['rate'])
    print(response[0]['companiesAffected'])
    return

if __name__ == '__main__':
    news()