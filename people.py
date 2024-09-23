import yaml
import json

with open("./data/people.yml", encoding="utf-16") as f:
    data = yaml.safe_load(f)

# print(data)

def get_job(name):
    for person in data["people"]:
        if person["name"] == name:
            return person["job"]
        
# print(get_job("Craig"))

def get_interests(name):
    for person in data["people"]:
        if person["name"] == name:
            return person["interests"]
        
# print(get_interests("Craig"))

def calculate_average_age():
    """
    Considers integer values as valid ages

    Calculates average based on valid ages and their respective person

    Returns an integer
    """
    valid_ages = [person["age"] for person in data["people"] if isinstance(person["age"], int)]
    return sum(valid_ages) // len(valid_ages)

# print(calculate_average_age())

def get_list_of_dicts():
    return data["people"]

# print(get_list_of_dicts())

def get_people_who_like_tombolas():
    return [person for person in data["people"] if "Tombolas" in person["interests"]]    

# print(get_people_who_like_tombolas())

def add_person_to_yaml_file(person_to_add):
    data["people"].append(person_to_add)
    with open("./data/people.yml", "w", encoding="utf-16") as f:
        yaml.dump(data, f)

# person_to_add = {"name": 'test', 'age': 30, 'job': 'test', 'interests': ['test'], 'wants': ['test'], 'location': 'test', 'favorite song': "test", 'favorite movie': "test"}

# add_person_to_yaml_file(person_to_add)

def add_fav_colour_key_to_data():
    for person in data["people"]:
        person["fav_colour"] = None
    with open("./data/people.yml", "w", encoding="utf-16") as f:
        yaml.dump(data, f)

# add_fav_colour_key_to_data()

def rewrite_london_as_the_city():
    for person in data["people"]:
        if person["location"] == "London":
            person["location"] = "The City"
    with open("./data/people.yml", "w", encoding="utf-16") as f:
        yaml.dump(data, f)

# rewrite_london_as_the_city()