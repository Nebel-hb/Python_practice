import json
menu = [
    {'name': 'ハンバーガー', 'price': 100, 'calorie': 260},
    {'name': 'チーズバーガー', 'price': 130, 'calorie': 310},
    {'name': 'フライドポテト', 'price': 150, 'calorie': 420}
]
with open('menu.txt', 'w') as file:
    json.dump(menu, file)
