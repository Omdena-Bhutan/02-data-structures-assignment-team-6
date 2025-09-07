#Part 1
character_profile={"Name":"Alistair the Brave",
                   "Level":1,
                   "Health":100,
                   "mana":50,
                   "Gold":50.75,
                   "Is_Alive":True}
print(f"Character: {character_profile['Name']}, Level: {character_profile['Level']}")
character_profile["Health"]=85
character_profile["Experience"]=0
print("\n--- Character Profile ---")
print(character_profile)


#Part 2
inventory=['Sword','Shield',' health portion']
inventory.append("mana portion")
inventory.remove("Shield")
print("\n--- Inventory ---")
for i in inventory:
  print(i)


#part 3
base_stats=(10,8,12)

strength = base_stats[0]
dexterity = base_stats[1]
intelligence = base_stats[2]
print("\n--- Base Stats ---")
print("Intelligence: ",intelligence)
print("Tuples are a good choice for stats because they are immutable (cannot be changed).")
#Challenge: Try to change a value (this will cause an error if uncommented)
# base_stats[0] = 15  # TypeError: 'tuple' object does not support item assignment


#part 4
quest_log={'Defeat the Goblin King', 'Find the Lost Amulet'}
quest_log.add("Deliver The Old Scroll")
# Add a duplicate quest (ignored automatically)
quest_log.add('Defeat the Goblin King')
quest_log.remove("Find the Lost Amulet")
print("\n--- Quest Log ---")
print(quest_log)

#part 5
character_sheet={"Profile": character_profile,
                 "Inventory": inventory,
                 "Stats":base_stats,
                 "Quest":quest_log}
print("\n---  Final Character Sheet ---")
print(character_sheet,"\n")
