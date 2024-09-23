import csv

def csv_to_dict(filepath):
    with open(filepath, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)
    
pizza_dicts = csv_to_dict("./data/pizza.csv")
print(pizza_dicts)

def get_ingredients(list_of_pizza_dicts, pizza):
    for pizza_dict in list_of_pizza_dicts:
        if pizza_dict["Pizza"] == pizza:
            return pizza_dict["Description"].split(", ")
        
capri_ingredients = get_ingredients(pizza_dicts, "Capri")
print(capri_ingredients)