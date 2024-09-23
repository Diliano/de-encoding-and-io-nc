import json

def json_to_list_of_dicts(filepath):
    with open(filepath, encoding="utf-16") as f:
        return json.load(f)["Cars"]
    
car_data = json_to_list_of_dicts("./data/cars.json")
# print(car_data)

def find_car_makes(car_data):
    return {car_dict["make"] for car_dict in car_data}

# print(find_car_makes(car_data))