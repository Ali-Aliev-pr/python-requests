import requests
import json

arrayForUsers = []

def get(id):
    url = f'https://reqres.in/api/users/{id}'
    response = requests.get(url)
    # print(response.text)
    response = json.loads(response.text)
    return response

def aray():
  # print(get(3))
  i = 1
  while True:
    # print(get(i))
    arrayForUsers.append(get(i))
    i+=1
    if get(i) == {}:
      break
  print(arrayForUsers)
aray()

def preobr(array):
  with open('index.txt', 'w') as outfile:
    json.dump(array, outfile)

preobr(arrayForUsers)