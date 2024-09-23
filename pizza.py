import csv

def csv_to_dict(filepath, encoding="utf-8"):
    with open(filepath) as f:
        reader = csv.DictReader(f)
        return list(reader)
    
pizza_dicts = csv_to_dict("./data/pizza.csv")
print(pizza_dicts)

def get_ingredients(list_of_pizza_dicts, pizza):
    for dict in list_of_pizza_dicts:
        if dict["Pizza"] == pizza:
            return dict["Description"].split(",")
        
capri_ingredients = get_ingredients(pizza_dicts, "Capri")
print(capri_ingredients)