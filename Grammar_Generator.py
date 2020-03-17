# Author - Ranjith Dhanaraj
# Prefunctory understanding of tracery is required to understand 
# grammar generation .Transitive verbs were manually edited to 
# enahnce the sentence structure. 

import pandas as pd

# File Operations
output = open("Grammar.txt", "w+", encoding="utf-8")

# Reading the dataset
superheroes_data = pd.read_excel("Veale's superheroes.xlsx", index_col = False)
city_data = pd.read_csv("world-cities_csv.csv")

# Selecting individual variables (columns) and formatting the data to better suit 
# grammar generation
crude_action = list(superheroes_data.iloc[:, 0])
action = [temp.replace("_", " ") for temp in crude_action]
crude_superhero = list(superheroes_data.iloc[:, 1].fillna("All Might"))
superhero = [temp.replace(",", "\", \"") for temp in crude_superhero]
crude_supervillian = list(superheroes_data.iloc[:, 2].fillna("Deku"))
supervillian = [temp.replace(",", "\", \"") for temp in crude_supervillian]

cities = list(city_data.iloc[:, 0])
countries = list(city_data.iloc[:, 1])

# Tracery grammar begins
output.write("{\n")
# Creating prefix and suffix nodes. 
# Prefix contains the characters and transitive verbs.
# Suffix contains the location of the encounter.
output.write("\"origin\" : [\"#prefix#. #suffix#\"],\n")
output.write("\n")

# Suffix node definition.
output.write("\"suffix\" : [\"They first encountered each other in the city of #location#\"],\n")
output.write("\n")

output.write("\"location\" : [\n")
for i, location in enumerate(cities):
    # Combining the name of the city with the country.
    # Eg. Dublin, Ireland.
    complete_location = cities[i] + ", " + countries[i]
    if (i < len(cities) - 1):
        output.write("\"" + complete_location + ".\", ")
    else:
        output.write("\"" + complete_location + ".\"],")
    output.write("\n")
output.write("\n\n")

# Preifx node definition.
output.write("\"prefix\" : [\n")

# Generating different non-terminal nodes for 'prefix'
for i, val in enumerate(crude_action):
    if(i < len(crude_action) - 1):
        output.write("\t\"#" + val + "#\",")
    else:
        output.write("\t\"#" + val + "#\"],")    
    output.write("\n")
output.write("\n")

# Generating sentences which are terminal. 
# Varible data(rows) is generated as well.
for i, val in enumerate(crude_action):
    # Grammar generation for nodes just before the last node.
    if(i < len(crude_action) - 1):
        output.write(("\"" + val + "\" : [\"#superhero_" + str(i) +
                    "# #action_" + str(i) + "# #supervillian_" + str(i) + "#\"],"))
        output.write("\n\"superhero_" + str(i) + "\" : [\"" + superhero[i] + "\"],")
        output.write("\n\"supervillian_" + str(i) + "\" : [\"" + supervillian[i] + "\"],")
        output.write("\n\"action_" + str(i) + "\" : [\"" + action[i] + "\"],")
    # Grammar generation for nodes on the last node.
    else:
        output.write(("\"" + val + "\" : [\"#superhero_" + str(i) +
                    "# #action_" + str(i) + "# #supervillian_" + str(i) + "#\"],"))
        output.write("\n\"superhero_" + str(i) + "\" : [\"" + superhero[i] + "\"],")
        output.write("\n\"supervillian_" + str(i) + "\" : [\"" + supervillian[i] + "\"],")
        output.write("\n\"action_" + str(i) + "\" : [\"" + action[i] + "\"]")
    output.write("\n\n")

output.write("\n")

output.write("}")
output.close()