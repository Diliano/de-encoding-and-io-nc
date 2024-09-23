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