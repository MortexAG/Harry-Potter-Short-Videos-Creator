import requests
import json
import spells_database

def get_characters():
    url = "https://hp-api.onrender.com/api/characters"
    response = requests.get(url)
    data = response.json()
    characters = []
    with open("characters.json", "w") as characters_list:
        for  i in data:
            characters.append(i)
        #indentation = len(characters)
        characters_json = json.dumps(characters, indent=2)
        characters_list.write(characters_json)
        

def get_spells_txt():
    url ="https://hp-api.onrender.com/api/spells"

    response = requests.get(url)
    data = response.json()
    spells = []
    count = 0
    for i in data:
        count += 1
        name = i["name"]
        description = i["description"]
        spell = f"\n{count}-{name} : {description}\n"
        spells.append(spell)
        #print(spell)
    with open("spells.txt", "w") as spells_text:
      for item in spells:
           spells_text.write(item)

def get_spells_json():
    url ="https://hp-api.onrender.com/api/spells"

    response = requests.get(url)
    data = response.json()
    spells = []
    spell_des_pairs = []
    for i in data:
        spells.append(i)
        spell_description = (i['name'], i['description'])
        spell_des_pairs.append(spell_description)
    with open("spells.json", "w") as spells_text:
        spells_json = json.dumps(spells, indent=2)
        spells_text.write(spells_json)
    for spell,description in spell_des_pairs:
        spells_database.insert_key_value(spell, description)
    spells_database.close_connection()
#get_characters()
get_spells_json()