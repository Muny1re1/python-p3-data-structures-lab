spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names_list = []
    for cuisine in spicy_foods:
        name = cuisine["name"]
        names_list.append(name)
    return names_list

def get_spiciest_foods(spicy_foods):
    spicy_foods_list = []
    for cuisine in spicy_foods:
        heat_level = cuisine.get("heat_level")
        if heat_level > 5:
            spicy_foods_list.append(cuisine)
    return spicy_foods_list

def print_spicy_foods(spicy_foods):
    emoji = "🌶"
    for cuisine in spicy_foods:
        name = cuisine.get("name")
        cuisine_origin = cuisine.get("cuisine")
        heat_level = cuisine.get("heat_level")
        hot = emoji * heat_level 
        print(f"{name} ({cuisine_origin}) | Heat Level: {hot}")
        

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    emoji = "🌶"
    for cuisine in spicy_foods:
        heat_level = cuisine.get("heat_level")
        if heat_level > 5:
            name = cuisine.get("name")
            cuisine_origin = cuisine.get("cuisine")
            hot = emoji * heat_level
            print(f"{name} ({cuisine_origin}) | Heat Level: {hot}")

def get_average_heat_level(spicy_foods):
    heat_levels = []
    for cuisine in spicy_foods:
        heat_level = cuisine.get("heat_level")
        heat_levels.append(heat_level)
    average_heat_level = sum(heat_levels) / len(heat_levels)
    return average_heat_level

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
