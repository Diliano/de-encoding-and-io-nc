import json

def json_to_list_of_dicts(filepath):
    with open(filepath, encoding="utf-8") as f:
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

def add_car_to_data(filepath, car_to_add):
    with open(filepath, "r+", encoding="utf-8") as f:
        read_f = json.load(f)
        read_f["Cars"].append(car_to_add)
        f.seek(0)
        json.dump(read_f, f, indent=4)

# car_to_be_added = {
#     "vin": "WAUHE78P29A814235",
#     "make": "Rivian",
#     "model": "RX1",
#     "year": 2008,
#     "colour": "Black"
# }
# add_car_to_data("./data/cars.json", car_to_be_added)

def update_year(filepath, vin, year):
    with open(filepath, "r+", encoding="utf-8") as f:
        read_f = json.load(f)
        for car_dict in read_f["Cars"]:
            if car_dict["vin"] == vin:
                car_dict["year"] = year
        f.seek(0)
        json.dump(read_f, f, indent=4)

# update_year("./data/cars.json", "WVGAV3AX5EW889767", 1985)