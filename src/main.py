import json
from data.ingredient_extraction import get_ingredients   
from model.allergen_detection import check_allergy
from utils.risk_calculator import calculate_risk

# ===============================
# Load datasets
# ===============================
with open("dataset/process/menu_uncertainty.json") as f:
    menu_uncertainty = json.load(f)

with open("dataset/process/allergen_labels.json") as f:
    allergen_labels = json.load(f)

# ===============================
# Menu Category Mapping
# ===============================
MENU_CATEGORY_MAP = {
    "somtam": "somtam",
    "padthai": "padthai",
    "pad_krapao": "pad_krapao",
    "tomyum": "tomyum",
}

def get_menu_category(menu_name):
    for key in MENU_CATEGORY_MAP:
        if menu_name.startswith(key) or key in menu_name:
            return MENU_CATEGORY_MAP[key]
    return menu_name.split("_")[0]  # fallback

# ===============================
# Input
# ===============================
menu_name = "padthai_chicken"
user_allergy = ["shellfish", "fish", "peanut"]

# ===============================
# Pipeline
# ===============================
# 1. Get ingredients from menu
ingredients = get_ingredients(menu_name)

# 2. Check allergens from ingredients
found_allergys = check_allergy(ingredients, user_allergy)

# 3. Get menu category
menu_category = get_menu_category(menu_name)

# 4. Calculate risk based on menu category and uncertainty
result = calculate_risk(menu_category, user_allergy, allergen_labels, menu_uncertainty)

# 5. Combine found allergens with risk result
result["found_allergen_from_ingredients"] = found_allergys

# ===============================
# Output
# ===============================
print("MENU:", menu_name)
print("INGREDIENT:", ingredients)
print("YOUR ALLERGY:", user_allergy)
print("FOUND ALLERGEN:", found_allergys)
print("RESULT:")
for key, value in result.items():
    print(f"  {key}: {value}")