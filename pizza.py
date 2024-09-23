import csv

def csv_to_dict(filepath, encoding="utf-8"):
    with open(filepath) as f:
        reader = csv.DictReader(f)
        return list(reader)
    
print(csv_to_dict("./data/pizza.csv"))