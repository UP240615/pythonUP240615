brother = ("Diego", "Mauricio")
sister = ("Mariana", "Sofia")
sibling = brother + sister
print(f"I have {len(sibling)} siblings")
family_members = sibling + ("Diego","Margarita")

sibling = family_members[:len(sibling)]
parents = family_members[-2:]
print(sibling, parents)

fruit = ("Mango", "Banana", "Grape")
veggies = ("Carrot", "Onion", "Potato")
animal_product = ("Bacon", "Egg", "Butter")

food_stuff_tp = fruit + veggies + animal_product
print(food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

mid = int(len(food_stuff_tp)/2)
food_stuff_tp = food_stuff_tp[:mid]
print(food_stuff_tp)

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)

