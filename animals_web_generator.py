import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')
print(animals_data)

output = ''

for animal in animals_data:
    name = animal.get('name', 'Unbekannt')
    locations = animal.get('locations', [])
    characteristics = animal.get('characteristics', {})
    diet = characteristics.get('diet', 'N/A')
    animal_type = characteristics.get('type', 'N/A')

    # Ausgabe
    # print("Name:", name)
    # print("Diet:", diet)
    # print("Location:", locations)
    # print("Type:", animal_type)
    # print()

    output += f"Name: {name}\n"
    output += f"Diet: {diet}\n"
    output += f"Location: {locations}\n"
    output += f"Type: {animal_type}\n\n"

print(output)

with open('animals_template.html', 'r') as file:
    template = file.read()

template = template.replace('__REPLACE_ANIMALS_INFO__', output)
print(template)

with open('animals.html', 'w') as file:
    file.write(template)
