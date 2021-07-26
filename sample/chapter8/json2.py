import json
with open('menu.txt', 'r') as file:
    menu = json.load(file)
print(menu)
