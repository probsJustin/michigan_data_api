import requests
import json


def get_json(data_url):
    print(f'Gathering data for: {data_url}')
    data = json.loads(requests.get(data_url).content)
    return data

def get_keys_of_data_set(data_set):
    return data_set[0].keys()
