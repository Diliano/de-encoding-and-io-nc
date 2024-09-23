import yaml

with open("./data/people.yml", encoding="utf-16") as f:
    data = yaml.safe_load(f)

# print(data)

def get_job(name):
    for person in data["people"]:
        if person["name"] == name:
            return person["job"]
        
# print(get_job("Craig"))