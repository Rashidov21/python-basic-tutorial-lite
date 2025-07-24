import json
import requests
# print(dir(json))

# dump , dumps, load, loads

d = {
  "name": "Ali",
  "age": 25,
  "work": "Dasturchi"
}

print(type(d)) # dict

# json ga olib o'tish
data = json.dumps(d)
print(type(data)) # <class 'str'>
# jsondan dict ga olib o'tish
data = json.loads(data)
print(type(data)) # <class 'dict'>


users_url = "https://jsonplaceholder.typicode.com/users"
users_data = requests.get(users_url)
print(users_data.json()) # data ni json korinishda olish
print(type(users_data.json())) # <class 'list'>
for i in users_data.json():
    print(type(i))