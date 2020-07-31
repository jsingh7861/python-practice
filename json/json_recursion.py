import requests
import json

def get_user(username):
    response = request.get(https://users.myorg.com/people?u=username)
    with open('response', 'r') as f:
        data = json.load(f)
        result_list = data.get('subordinates')
        for i in result_list():
            print(i)
            username = i 
            get_user(username)
