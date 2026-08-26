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
    locations = animal.get('locations', [])[0]
    characteristics = animal.get('characteristics', {})
    diet = characteristics.get('diet', 'N/A')
    animal_type = characteristics.get('type', 'N/A')

    # Ausgabe
    # print("Name:", name)
    # print("Diet:", diet)
    # print("Location:", locations)
    # print("Type:", animal_type)
    # print()
    output += '<li class="cards__item">'
    output += f"<div class=\"card__title\">{name}</div>"
    output += f"<p class =\"card__text\" >"
    output += f"<strong>Diet:</strong> {diet}<br/>"
    output += f"<strong>Location:</strong> {locations}<br/>"
    output += f"<strong>Type:</strong> {animal_type}<br/>"

    output += "</p>"

    output += '</li>'
print(output)

with open('animals_template.html', 'r') as file:
    template = file.read()

template = template.replace('__REPLACE_ANIMALS_INFO__', output)
print(template)

with open('animals.html', 'w') as file:
    file.write(template)
