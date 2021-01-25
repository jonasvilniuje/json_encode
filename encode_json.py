# read json
# select only json keys and str values
# encode every kv
# assign value to json object
# convert to json

import json

file = "json.txt"
json_content = ""

with open(file) as f:
    json_content = json.load(f)
    
