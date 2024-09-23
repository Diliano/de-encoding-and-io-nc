import csv

def csv_to_dict(filepath):
    with open(filepath, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)
    
pizza_dicts = csv_to_dict("./data/pizza.csv")
# print(pizza_dicts)

def get_ingredients(list_of_pizza_dicts, pizza):
    for pizza_dict in list_of_pizza_dicts:
        if pizza_dict["Pizza"] == pizza:
            return pizza_dict["Description"].split(", ")
        
capri_ingredients = get_ingredients(pizza_dicts, "Capri")
# print(capri_ingredients)

def get_pizzas_under_9(list_of_pizza_dicts):
    pizzas_under_9 = [pizza_dict for pizza_dict in list_of_pizza_dicts if float(pizza_dict["Cost"][1:]) < 9]
    return sorted(pizzas_under_9, key=lambda x: float(x["Cost"][1:]))

# print(get_pizzas_under_9(pizza_dicts))

def write_pizza_to_file(filepath, pizza_to_add):
    with open(filepath, "a", encoding="utf-8") as f:
        fieldnames = ["Pizza", "Cost", "Description", "Calories"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(pizza_to_add)

# write_pizza_to_file("./data/pizza.csv", {"Pizza": "Pepperoni", "Cost": "£6.50", "Description": "Vegan cheese, vegan pepperoni, mushroom, sweetcorn", "Calories": "710kcal"})

def increase_pizza_costs(filepath, list_of_pizza_dicts):
    for pizza_dict in list_of_pizza_dicts:
        old_cost = float(pizza_dict["Cost"][1:])
        new_cost = old_cost + (old_cost * 0.1)
        pizza_dict["Cost"] = f"£{new_cost:.2f}"
    
    with open(filepath, "w", encoding="utf-8") as f:
        fieldnames = ["Pizza", "Cost", "Description", "Calories"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(list_of_pizza_dicts)

# increase_pizza_costs("./data/pizza.csv",pizza_dicts)