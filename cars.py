import json

def json_to_list_of_dicts(filepath):
    with open(filepath, encoding="utf-16") as f:
        return json.load(f)["Cars"]
    
# print(json_to_list_of_dicts("./data/cars.json"))