import json

def json_to_list_of_dicts(filepath):
    with open(filepath, encoding="utf-16") as f:
        return json.load(f)["Cars"]
    
car_data = json_to_list_of_dicts("./data/cars.json")
# print(car_data)

def get_car_makes(car_data):
    return {car_dict["make"] for car_dict in car_data}

# print(get_car_makes(car_data))

def get_cars_under_20_years_old(car_data):
    cars_under_20 = \
    [car_dict for car_dict in car_data if (2024 - car_dict["year"]) < 20]
    return sorted(cars_under_20, key=lambda x: x["year"], reverse=True)

# print(get_cars_under_20_years_old(car_data))