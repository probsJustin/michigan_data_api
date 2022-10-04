import requests
import json

import modules.util as util
import modules.data as data


data_urls = data.get_data()

data_set = util.get_json(data_urls['michigan_fish'])
data_set_keys = util.get_keys_of_data_set(data_set)

print(data_set_keys)
print(data_set)