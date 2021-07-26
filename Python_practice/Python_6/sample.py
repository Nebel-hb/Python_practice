import json
with open('menu.text', 'r')as file:
        menu = json.load(file)
print(menu)