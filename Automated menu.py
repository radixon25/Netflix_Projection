import random
days = ["Fri","Sat","Sun","Mon", "Tues","Wed","Thurs"]
all_dishes_dict = {"Chinese" : ["Shrimp Fried Rice" , "BAKED GENERAL TSO CHICKEN", "SLOW COOKER BROCCOLI BEEF", "SKINNY ORANGE CHICKEN" , "Spicy Beef & Pepper Stir-Fry", "Beef & Spinach Lo Mein"] ,"Korean" : ["Korean fried chicken"] ,"Japanese" : [],"Mexican" : ["Fish Tacos"],"Indian" : ["butter chicken"],"Carribean": ["Puerto Rican Chicken and Rice"]}
healthy_dishes_dict = {"Chinese" : ["Shrimp Fried Rice" , "BAKED GENERAL TSO CHICKEN", "SLOW COOKER BROCCOLI BEEF", "SKINNY ORANGE CHICKEN" ] ,"Korean" : [],"Japanese" : [],"Mexican" : [],"French" : [],"Indian" : [],"Carribean": [],"American" : []}
countries = []
menu = []
count_yes = 0
regular_recipes = { "butter chicken": "https://cafedelites.com/butter-chicken/", "Fish Tacos" : "https://cooking.nytimes.com/recipes/1012445-fish-tacos" , "Korean fried chicken" : "https://www.bbcgoodfood.com/recipes/korean-fried-chicken" , "Puerto Rican Chicken and Rice" : "https://www.ambitiouskitchen.com/puerto-rican-chicken-and-rice-arroz-con-pollo/"}
healthy_recipes = {"BAKED GENERAL TSO CHICKEN" : "https://pickledplum.com/baked-general-tso-chicken-recipe/?utm_content=bufferade7c&utm_medium=social&utm_source=pinterest.com&utm_campaign=buffer","SLOW COOKER BROCCOLI BEEF" : "https://www.lecremedelacrumb.com/slow-cooker-broccoli-beef","SKINNY ORANGE CHICKEN" : "https://addapinch.com/skinny-orange-chicken-recipe/"}
all_recipes = dict(regular_recipes)
all_recipes.update(healthy_recipes)
def     getList(dict):

    return list(dict.keys())

reg_dishes = getList(regular_recipes)
healthy_dishes = getList(healthy_recipes)
print("Do you want to add any recipes? (y/n)")
new_recipes = input()
if new_recipes == "y":
    print("How many?")
    number = input()
    for i in range(int(number)):
        print("What country is the recipe from? (Chinese, Korean, Japanese, Mexican, French, Indian, Carribean, or American)")
        new_country = input()
        print("What is the dish called?")
        new_dish = input()
        print("Recipe URL: ")
        new_url = input()
        print("Is this recipe Healthy (y/n)")
        healthy = input()
        if new_country in all_dishes_dict:
            if healthy == "y":
                all_dishes_dict[new_country].append(new_dish)
                healthy_dishes_dict[new_country].append(new_dish)
                recipes[new_dish] = new_url
            elif healthy == "n":
                all_dishes_dict[new_country].append(new_dish)
                recipes[new_dish] = new_url
        else:
            print("This country needs added to the list.")
    print("Let's pick this weeks recipes")
else:
    print("Let's pick this weeks recipes")
          
for i,word in enumerate(days):
    print("Are we eating healthy on {} (y/n)".format(days[i]))
    diet = input ()
    if diet == "y":
        count_yes = count_yes + 1
healthy_menu = random.sample(healthy_dishes,count_yes)
regular_menu = random.sample(reg_dishes,7-count_yes)
menu = healthy_menu + regular_menu
print(menu)
for i,w in enumerate(menu):
    print("{}'s dish is {}, and the recipe is on {}.".format(days[i],menu[i],all_recipes[menu[i]]))