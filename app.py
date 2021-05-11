import requests
import json

def her(country, page):
    def save_photo(link, name):
        response = requests.get(link)
        with open(f'images/{name}.png', 'wb') as f:
            f.write(response.content)

    url = f'https://www.chess.com/callback/leaderboard/live?country={country}&page={page}'
    response = requests.get(url)
    print(response.text)
    response = json.loads(response.text)
    # print(response)
    for i in response['leaders']:
        save_photo(i['user']['avatar_url'], i['user']['username'])

    

her('US', 2)