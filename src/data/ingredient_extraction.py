import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path = os.path.join(BASE_DIR, 'dataset/raw/ingredients.json')

with open(file_path, 'r') as f:
    data = json.load(f)

def get_ingredients(menu_name) :
    
    for category in data:
        menu = data[category]
        if menu_name in menu:
            return menu[menu_name]
            
    return "Menu not found"

