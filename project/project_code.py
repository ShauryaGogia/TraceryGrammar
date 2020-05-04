import requests
import random
import re

''' Function to create new spells based on spell actions
    Input: Harry Potter spell dict, D&D spell dict, action
    Output: dictionary with newly created spells as keys and their descriptions as values
'''
def find_matching_spells(hp_dict, dd_dict, word):
    spells_dict = {}
    dict1 = {}
    dict2 = {}
    for key, value in hp_dict.items():
        if value.lower().find(word) >= 0:
            dict1[key] = value.lower() # Creating new dictionary having only those key-value pairs from HP dict which contain the action word in the value 
    
    for key, value in dd_dict.items():
        if value.lower().find(word) >= 0:
            dict2[key] = value.lower() # Creating new dictionary having only those key-value pairs from DD dict which contain the action word in the value
    
    list_dict1_keys = list(dict1.keys())
    list_dict1_values = list(dict1.values())
    list_dict2_keys = list(dict2.keys())
    list_dict2_values = list(dict2.values())
    list_dd_dict_keys = list(dd_dict.keys())
    list_dd_dict_values = list(dd_dict.values())
    list_hp_dict_keys = list(hp_dict.keys())
    list_hp_dict_values = list(hp_dict.values())
    
    if len(dict1) > 0:
        for i in range(0, len(dict1)): # Iterating over all the key-value pairs in the above created dictionary for hp_dict
            index = random.randint(0, len(dd_dict) - 1) # taking a random number as index 
            key = list_dict1_keys[i] + " " + list_dd_dict_keys[index] # New spell = hp_action_spell + " " + dd_random_spell 
            list_dd_dict_values[index] = re.sub('"', '', list_dd_dict_values[index]) 
            list_dict1_values[i] = re.sub('"', '', list_dict1_values[i])
            spells_dict[key] = list_dict1_values[i] + " and " + list_dd_dict_values[index].lower().split('.')[0].strip() # New spell description = hp_action_description + " and " + first sentence of dd_random_description 
    if len(dict2) > 0: 
        for i in range(0, len(dict2)): # Iterating over all the key-value pairs in the above created dictionary for dd_dict
            index = random.randint(0, len(hp_dict) - 1) # taking a random number as index 
            key = list_dict2_keys[i] + " " + list_hp_dict_keys[index] # New spell = dd_action_spell + " " + hp_random_spell
            split_list = list_dict2_values[i].split(".")
            for sentence in split_list:
                if sentence.find(word) >= 0:
                    break
            sentence = re.sub('[^A-Za-z0-9- ]+', '', sentence)
            sentence = re.sub('"', '', sentence)
            list_hp_dict_values[index] = re.sub('"', '', list_hp_dict_values[index])
            spells_dict[key] = sentence.strip() + " and " + list_hp_dict_values[index].lower() # New spell description = relevant sentence of dd_action_description + " and " + hp_random_description
    
    return spells_dict if len(spells_dict) > 0 else "no matching spells"

# Gets response of invoking Harry Potter API
hp_spells = requests.get("https://www.potterapi.com/v1/spells?key=$2a$10$YdQG8g5qSs3wumPzsqv6ReHDDZhzdHGpW5vq3SjYz0O.I9GAoMfWG").json()

dd_spells = []
for i in range(1,8): # Gets response of invoking D&D API and iterates over 7 pages
    dd_spells.extend(list(requests.get("https://api.open5e.com/spells/?page=" + str(i)).json()['results']))

hp_spells_dict = {}
# Extracts the required information from the response of the API and creates a dictionary with key as Spell Name and value as Spell Description
for response in hp_spells:
    hp_spells_dict[response['spell']] = response['effect']

dd_spells_dict = {}
# Extracts the required information from the response of the API and creates a dictionary with key as Spell Name and value as Spell Description
for response in dd_spells:
    dd_spells_dict[response['name']] = response['desc']

# Grammar Code
# Opens files in write mode
original_grammar_file = open("spellteller1_original_grammar.txt", "w+", encoding = "utf-8")
response_grammar_file = open("spellteller1_response_grammar.txt", "w+", encoding = "utf-8")
reply_grammar_file = open("sams2808_response_grammar.txt", "w+", encoding = "utf-8")

# Writes static rules in "spellteller1_original_grammar.txt" file
original_grammar_file.write("{\n")
original_grammar_file.write("\"origin\": [\"Its been long since I have helped anyone with my abilities. @Sams2808 would you like some magic?\"],\n")
original_grammar_file.write("\"magicline\": [\"Don't worry my child. I am here for you (though virtually). I know a lot of spells, what kind of spell do you need?\\n@Sams2808 category\"],\n")
original_grammar_file.write("\"categorybefore\": [\"#dr_strange#!!!\\nOkay, ummmmmmm,let me see. Why don't you take a shot at this spell. @Sams2808\"],\n")
original_grammar_file.write("\"dr_strange\": [\"By the Eye of Agamotto\", \"By the Images of Ikonn\", \"By the Ruby Rings of Raggadorr\", \"By the Crimson Bands of Cyttorak\", \"By the Flames of the Faltine\", \"By the Sons of Satannish\", \"By the Hoary Hosts of Hoggoth\", \"By the Ageless Vishanti\", \"By the Vapors of Valtorr\", \"By the Demons of Denak\", \"By the Fangs of Farallah\", \"By the Mystic Moons of Munnopor\", \"By the Shades of the Seraphim\", \"By the Shields of the Seraphim\", \"By the Omnipotent Oshtur\", \"By the Icy Tendrils of Ikthalon\", \"By the Chains of Krakkan\", \"By the Wondrous Winds of Watoomb\"],\n")
original_grammar_file.write("\"afterspell\": [\". @Sams2808 tell me after casting it. But please don't attempt it at home.\"],\n")
original_grammar_file.write("\"thanksline\": [\"You go girllll :P\"],\n")
original_grammar_file.write("\"moneyline\": [\"HESOYAM!!! Are you playing GTA San Andreas ! Asking for money spells even in these times. Pathetic. Do you want some other spell or should I just leave?\\n@Sams2808 other\"],\n")
original_grammar_file.write("\"loveline\": [\"helloladies!!! Are you playing GTA San Andreas ! Asking for love spells. Find some love guru, you pathetic soul. Do you want some other spell or should I just leave?\\n@Sams2808 other\"],\n")
original_grammar_file.write("\"defaultline\": [\"I don't know any spell of this category. Do you want some other?\\n@Sams2808 another\"],\n")
original_grammar_file.write("\"amazingline\": [\"I know I am amazing.\\n@Sams2808 next\"],\n")
original_grammar_file.write("\"horribleline\": [\"DUUHHHH!!! I am not GOD, won't always be right. Magic is experimental, but still I will apologize.\\n@Sams2808 try again\"],\n")

# Writes static rules in "spellteller1_response_grammar.txt" file
response_grammar_file.write("{\n")
response_grammar_file.write("\"[H|h][E|e][L|l][P|p]\": \"#magicline#\",\n")
response_grammar_file.write("\"[A|a][M|m][A|a][Z|z][I|i][N|n][G|g]\": \"#amazingline#\",\n")
response_grammar_file.write("\"[H|h][O|o][R|r][R|r][I|i][B|b][L|l][E|e]\": \"#horribleline#\",\n")
response_grammar_file.write("\"[T|t][H|h][A|a][N|n][K|k][S|s]\": \"#thanksline#\",\n")
response_grammar_file.write("\"[M|m][O|o][N|n][E|e][Y|y]\": \"#moneyline#\",\n")
response_grammar_file.write("\"[H|h][E|e][A|a][L|l][T|t][H|h]\": \"#moneyline#\",\n")
response_grammar_file.write("\"[L|l][O|o][V|v][E|e]\": \"#loveline#\",\n")

# Writes static rules in "sams2808_response_grammar.txt" file
reply_grammar_file.write("{\n")
reply_grammar_file.write("\"[W|w][O|o][U|u][L|l][D|d]\": \"#magicline#\",\n")
reply_grammar_file.write("\"[T|t][R|r][Y|y]\": \"#tryline#\",\n")
reply_grammar_file.write("\"[N|n][E|e][X|x][T|t]\": \"#nextline#\",\n")
reply_grammar_file.write("\"[C|c][A|a][T|t][E|e][G|g][O|o][R|r][Y|y]\": \"#categoryline#\",\n")
reply_grammar_file.write("\"[O|o][T|t][H|h][E|e][R|r]\": \"#otherline#\",\n")
reply_grammar_file.write("\"[A|a][N|n][O|o][T|t][H|h][E|e][R|r]\": \"#missingcategoryline#\",\n")
reply_grammar_file.write("\"[T|t][E|e][L|l][L|l]\": \"#endline#\",\n")

# Self-identified list of spell actions                         
actions = ['shadow', 'summon', 'teleport', 'cure', 'heal', 'fly', 'open', 'change', 'control', 'water', 'blast', 'reveal', 'slow', 'moves', 'murder', 'explode', 'detect', 'emit', 'damage', 'torture', 'counter', 'enlarge', 'reduce', 'build', 'vanish', 'stop', 'duplicate', 'slow', 'fire', 'hang', 'animate', 'silence', 'switch']

# Dictionary to store all the spells generated for each category
all_spells = {}

# Iterating over all actions in the 'actions' list
for word in actions:
    spells = find_matching_spells(hp_spells_dict, dd_spells_dict, word) # calls the 'find_matching_spells' function
    if spells == "no matching spells":
        continue
    else:
        all_spells.update(spells) # updates the 'all_spells' dict with the dict returned from the function call
        list_keys = list(spells.keys())
        # Grammar code
        original_grammar_file.write("\"" + word + "\": [")
        response_grammar_file.write("\"")
        for j in range(0, len(word)):
            if j == len(word) - 1:
                response_grammar_file.write("[" + word[j].upper() + "|" + word[j] + "]\": ")
            else:
                response_grammar_file.write("[" + word[j].upper() + "|" + word[j] + "]")
        response_grammar_file.write("\"#categorybefore# ")
        response_grammar_file.write("#" + word + "#\",\n")
        for i in range(0,len(list_keys)):
            if i == len(list_keys) - 1:
                original_grammar_file.write("\"" + list_keys[i] + "\"],")
            else:
                original_grammar_file.write("\"" + list_keys[i] + "\", ")
        original_grammar_file.write("\n")

# Grammar code
for key, value in all_spells.items():
    original_grammar_file.write("\"" + key + "\": [\"" + value + "\"],")
    original_grammar_file.write("\n")
    response_grammar_file.write("\"")
    reply_grammar_file.write("\"")
    for i in range(0, len(key)):
        if i == len(key) - 1:
            response_grammar_file.write("[" + key[i].upper() + "|" + key[i] + "]\": ")
            reply_grammar_file.write("[" + key[i].upper() + "|" + key[i] + "]\": ")
        elif key[i] == ' ':
            response_grammar_file.write(" ")
            reply_grammar_file.write(" ")
        else:
            response_grammar_file.write("[" + key[i].upper() + "|" + key[i] + "]")
            reply_grammar_file.write("[" + key[i].upper() + "|" + key[i] + "]")
    response_grammar_file.write("\"#" + key + "# #afterspell#\",\n")
    reply_grammar_file.write("\"#spellline# " + key + "\",\n")
original_grammar_file.write("}")
original_grammar_file.close()
response_grammar_file.write("\".\": \"#defaultline#\"\n")
response_grammar_file.write("}")
response_grammar_file.close()
reply_grammar_file.write("}")
reply_grammar_file.close()