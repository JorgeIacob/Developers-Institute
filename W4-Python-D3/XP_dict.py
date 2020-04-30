#1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dictionary = dict(zip(keys, values))
print(dictionary)

#2
stores = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {"France": "blue", "Spain": "red", "US": ["pink", "green"]}
}

print(stores)
stores["number_stores"] = 2
print(stores["number_stores"])
stores["country_creation"] = "Spain"
print(stores)

if "international_competitors" in stores:
    stores['international_competitors'].append("Desigual")
print(stores["international_competitors"])
stores.pop('creation_date')
print(stores)
print(stores['international_competitors'][-1])

print(f'Major colors in the US are {stores["major_color"]["US"]}')

print(f'Length of Stores:{len(stores)}')
print(f'Keys of Stores:{stores.keys()}')

more_on_store = {
    'creation_date': 1975,
    'number_stores': 10000
}

stores.update(more_on_store)
print(f'Updated Stores:{stores}')
print(f'Updated Number of Stores :{stores["number_stores"]}')

stores_worldwide: dictionary = {}
if "stores_worldwide" not in stores:
    stores["stores_worldwide"] = stores_worldwide
print(f'Updated Stores with new dictionary stores_worldwide:{stores["stores_worldwide"]}')

#Bonus
def addStore(country: str, number: int):
    if "stores_worldwide" in stores:
        stores["stores_worldwide"][country] = number


addStore("Israel", 1)
print(f'Stores World Wide:{stores["stores_worldwide"]}')
