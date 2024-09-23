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

def get_pizzas_under_9(list_of_pizza_dicts):
    pizzas_under_9 = [pizza_dict for pizza_dict in list_of_pizza_dicts if float(pizza_dict["Cost"][1:]) < 9]
    return sorted(pizzas_under_9, key=lambda x: float(x["Cost"][1:]))

print(len(get_pizzas_under_9(pizza_dicts)))