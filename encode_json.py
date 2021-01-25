# read json
# select only json keys and str values
# encode every kv
# assign value to json object
# convert to json

import json

#convert string into escaped unicode codes
def str_to_esc_utf(s):
    a = ""
    
    if isinstance(s, str):
        for c in s.encode():
            a = a+("\\u"+str("{:04x}".format(c)))
        return a

    else: return s

def print_values(key, json_data):
    new_dict = {}
    if isinstance(json_data, dict):
        for k, v in json_data.items():
            if isinstance(v, dict):
                print_values(k, v)
            elif  isinstance(v, list):
                print_values(k, v)
            else: 
                new_dict[str_to_esc_utf(k)] = str_to_esc_utf(v)
                
                
    elif isinstance(json_data, list):
        
        _list = []
        _dict = {}
        
        for v in json_data:
            if isinstance(v, dict) or isinstance(v, list):
                print_values(key, v)
            else: 
                _list.append(str_to_esc_utf(v))
                _dict[str_to_esc_utf(key)] = _list
        
        new_dict[str_to_esc_utf(key)]=_dict
    
    else: print("err")
    
    return new_dict

file = "json.txt"
json_content = ""

with open(file) as f:
    json_content = json.load(f)
    
print_values('', json_content)
