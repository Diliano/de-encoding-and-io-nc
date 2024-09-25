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

print(get_cost_of_largest_detached_home_for_sale())