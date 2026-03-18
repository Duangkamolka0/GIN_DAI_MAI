import json

# =========================
# 1. LOAD DATASET
# =========================

with open("dataset/raw/ingredients.json", "r") as f:
    menu_ingredients = json.load(f)

with open("dataset/process/ingredients_allergen_mapping.json", "r") as f:
    data = json.load(f)
    ingredient_allergen_mapping = data["ingredient_allergen_map"]


# =========================
# 2. FUNCTION
# =========================

def build_menu_uncertainty(menu_ingredients, ingredient_allergen_mapping):
    menu_uncertainty = {}

    for menu, recipes in menu_ingredients.items():
        allergen_count = {}
        total_recipes = len(recipes)

        for recipe_name, ingredient_list in recipes.items():
            found_allergens = set()

            for ingredient in ingredient_list:
                if ingredient in ingredient_allergen_mapping:
                    for allergen in ingredient_allergen_mapping[ingredient]:
                        found_allergens.add(allergen)

            for allergen in found_allergens:
                allergen_count[allergen] = allergen_count.get(allergen, 0) + 1

        probs = {}
        for allergen, count in allergen_count.items():
            probs[allergen] = round(count / total_recipes, 2)

        menu_uncertainty[menu] = probs

    return menu_uncertainty


# =========================
# 3. RUN + SAVE
# =========================

if __name__ == "__main__":
    result = build_menu_uncertainty(menu_ingredients, ingredient_allergen_mapping)

    with open("menu_uncertainty.json", "w") as f:
        json.dump(result, f, indent=2)

    print("Saved menu_uncertainty.json")