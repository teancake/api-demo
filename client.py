import requests
import json

if __name__ == '__main__':
    # get method
    root_url = "http://127.0.0.1:8000"
    response = requests.get(root_url)
    print(response.json())

    # post method
    data = {"width": 1, "height": 1, "name": "who"}
    data_str = json.dumps(data)
    print(data_str)
    response = requests.post(root_url + "/predict", data=data_str)
    print(response.json())
