import requests
import json

URL = "http://localhost:3000/api/"

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    res = requests.get(url=URL, data=json_data)

    new_data = res.json()
    print(new_data)

get_data()