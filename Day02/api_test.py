# DevOps Engineer - Developer has an API(Application Programmable Interface)

import requests

def get_api_data():

    url = "https://jsonplaceholder.typicode.com/posts"
    #url = "https://reqres.in/api/users"

    response = requests.get(url)
    print(response.json()[2])

    return response.json()

get_api_data()
