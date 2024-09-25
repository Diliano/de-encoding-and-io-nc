import xml.etree.ElementTree as ET

tree = ET.parse("./data/properties.xml")
root = tree.getroot()

def get_cost_of_largest_detached_home_for_sale():
    result = []
    for sale in root.findall("sale"):
        for detached in sale.findall("detached"):
            for home in detached:
                sq_ft = int(home.find("plot_size").text[:-5])
                price = int(home.find("cost").text[1:])
                result.append((sq_ft, price))
    return sorted(result)[-1][1]

# print(get_cost_of_largest_detached_home_for_sale())

def get_description_of_third_home_from_bungalows_for_sale():
    for sale in root.findall("sale"):
        for bungalow in sale.findall("bungalow"):
            for home in bungalow.findall("home3"):
                return home.find("description").text
            
# print(get_description_of_third_home_from_bungalows_for_sale())

"""
Create a function that returns the number of bathrooms that
the first flat for rent has.
"""

def get_num_bathrooms_of_first_flat_for_rent():
    for sale in root.findall("rent"):
        for flat in sale.findall("flat"):
            for flat in flat.findall("flat1"):
                return int(flat.find("bathrooms").text)
            
# print(get_num_bathrooms_of_first_flat_for_rent())