# Author - Ranjith Dhanaraj
# Prefunctory understanding of tracery is required to understand 
# grammar generation
# Transitive verbs were manually edited to enahnce the sentence structure.

import pandas as pd

# File Operations
output = open("19200041_Ranjith_Dhanaraj_Grammar.txt", "w+", encoding="utf-8")

# Reading the dataset
superheroes_data = pd.read_excel("Veale's superheroes.xlsx", index_col = False)
city_data = pd.read_csv("world-cities_csv.csv")
sounds_data = pd.read_excel("Animal sounds.xlsx", index_col = False)
dream_data = pd.read_excel("Veale's Dream Symbols.xlsx", index_col = False)

# Selecting individual variables (columns) and formatting the data to better suit 
# grammar generation
crude_action = list(superheroes_data.iloc[:, 0])
action = [temp.replace("_", " ") for temp in crude_action]

crude_superhero = list(superheroes_data.iloc[:, 1].fillna("All Might, Deku, Astrostar"))
superhero = [temp.replace(",", "\", \"") for temp in crude_superhero]

crude_supervillian = list(superheroes_data.iloc[:, 2].fillna("Professor Funny, Agent Tag, The Cruel Knuckles"))
supervillian = [temp.replace(",", "\", \"") for temp in crude_supervillian]

crude_animals = list(sounds_data.iloc[:, 0])
animals = [temp.replace("_", " ") for temp in crude_animals]

crude_sounds = list(sounds_data.iloc[:, 1])
sounds = [temp.replace(" ", "") for temp in crude_sounds]
sounds = [temp.replace(",", "\", \"") for temp in sounds]
sounds = [temp.replace("ed", "ing") for temp in sounds]

crude_dream = list(dream_data.iloc[:, 2])
dream = [temp.replace("\"", "'") for temp in crude_dream]

adj = ["interesting", "different", "hot", 'exciting', 'regular', 'productive', 'tiring', 'cold', 'breezy', 'dull', "slow"]

cities = list(city_data.iloc[:, 0])
countries = list(city_data.iloc[:, 1])

# Tracery grammar begins

# Tracery grammar begins
output.write("{\n")
output.write("\"origin\" : [\"#part1#. #part2#. #part3# #part4#.\"],\n")
output.write("\n")

output.write("\"part1\" : [\"Hogwarts News reporting - It is #adj.a# day in the streets of #location#\"],\n")
output.write("\n")
output.write("\"location\" : [\n")
for i, location in enumerate(cities):
    # Combining the name of the city with the country.
    # Eg. Dublin, Ireland.
    complete_location = cities[i] + ", " + countries[i]
    if (i < len(cities) - 1):
        output.write("\"" + complete_location + "\", ")
    else:
        output.write("\"" + complete_location + "\"],")
output.write("\n\n")

output.write("\"adj\" : [")
for i, val in enumerate(adj):
    if i < len(adj) - 1:
        output.write("\"" + adj[i] + "\", ")
    else:
        output.write("\"" + adj[i] + "\"],\n")
output.write("\n\n")


output.write("\"part2\" : [\"#supervillian_base# transformed #superhero_base# into #transform# by the end of it\"],\n")

output.write("\"superhero_base\" : [")
for i, val in enumerate(crude_action):
    # Grammar generation for nodes just before the last node.
    if(i < len(crude_action) - 1):
        output.write("\"#superhero_" + str(i) + "#\", ")
    else:
        output.write("\"#superhero_" + str(i) + "#\"],\n")

output.write("\n\n")

output.write("\"supervillian_base\" : [")
for i, val in enumerate(crude_action):
    # Grammar generation for nodes just before the last node.
    if(i < len(crude_action) - 1):
        output.write("\"#supervillian_" + str(i) + "#\", ")
    else:
        output.write("\"#supervillian_" + str(i) + "#\"],\n")

# #animal.a# and they were just #sounds#
output.write("\n\n")

output.write("\"transform\" : [")
for i, val in enumerate(crude_animals):
    if(i < len(crude_animals) - 1):
        output.write("\"#" + val + "#\", ")
    else:
        output.write("\"#" + val + "#\"],\n")
    
output.write("\n\n")

for i, val in enumerate(crude_animals):
    output.write(("\"" + val + "\" : [\"#animals_" + str(i) + ".a# and the hero was just #sounds_" + str(i) + "#\"],"))
    output.write("\n\"animals_" + str(i) + "\" : [\"" + animals[i] + "\"],")
    output.write("\n\"sounds_" + str(i) + "\" : [\"" + sounds[i] + "\"],")
    output.write("\n\n")
    
output.write("\n\n")

output.write("\"part3\" : [\"In other news, #superhero_base# interpreted The Mayor's dream and said - #dream#\"],\n")
output.write("\"dream\" : [")
for i, val in enumerate(dream):
    if i < len(dream) - 1:
        output.write("\"" + val + "\", ")
    else:
        output.write("\"" + val + "\"],\n")
output.write("\n\n")

output.write("\"part4\" : [")
for i, val in enumerate(crude_action):
    if(i < len(crude_action) - 1):
        output.write("\"#" + val + "#\",")
    else:
        output.write("\"#" + val + "#\"],\n")    
output.write("\n\n")

for i, val in enumerate(crude_action):
        output.write(("\"" + val + "\" : [\"And top it all off a scoop - #superhero_" + str(i) +
                    "# #action_" + str(i) + "# #supervillian_" + str(i) + "#\"],"))
        output.write("\n\"superhero_" + str(i) + "\" : [\"" + superhero[i] + "\"],")
        output.write("\n\"supervillian_" + str(i) + "\" : [\"" + supervillian[i] + "\"],")    
output.write("\n\n")

for i, val in enumerate(crude_action):
    if(i < len(crude_action) - 1):
        output.write("\n\"action_" + str(i) + "\" : [\"" + action[i] + "\"],")    
    else:
        output.write("\n\"action_" + str(i) + "\" : [\"" + action[i] + "\"]")    

output.write("\n\n")
output.write("}")
output.close()
