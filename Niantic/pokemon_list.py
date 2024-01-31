'''
Question: Given a list of Pokemon and their rarities, pick a random pokemon. 
Rarity is defined such that the higher the rarity, the less likely the pokemon 
will appear on the map
Example:
Pikachu.rarity = 10; // Pikachu should appear 10x more often thanmewtwo
Mewtwo.rarity = 100;
'''
import bisect
import random

pokemons = {"Pikachu": 10, "Mewtwo": 100, "Golem": 50}

# build the rarity list
pokemon_list = []
prefix_sum = []
sum_rarity = 0
for key, value in pokemons.items():
    sum_rarity += 1 / value
    prefix_sum.append(sum_rarity)
    pokemon_list.append(key)
   
# random pick
pick_num = random.uniform(0, sum_rarity)
index = bisect.bisect_left(prefix_sum, pick_num)
print(pokemon_list[index])
