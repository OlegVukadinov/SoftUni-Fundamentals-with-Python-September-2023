heroes = {}

while True:
    command = input()
    if command == "End":
        break

    com = command.split(' ')
    action = com[0]


    if action == "Enroll":
        hero_name = com[1]
        if hero_name not in heroes:
            heroes[hero_name] = []
        else:
            print(f"{hero_name} is already enrolled.")
    elif action == "Learn":
        hero_name = com[1]
        spell_name = com[2]
        if hero_name in heroes:
            if spell_name not in heroes[hero_name]:
                heroes[hero_name].append(spell_name)
            else:
                print(f"{hero_name} has already learnt {spell_name}.")
        else:
            print(f"{hero_name} doesn't exist.")
    elif action == "Unlearn":
        hero_name = com[1]
        spell_name = com[2]
        if hero_name in heroes:
            if spell_name in heroes[hero_name]:
                heroes[hero_name].remove(spell_name)
            else:
                print(f"{hero_name} doesn't know {spell_name}.")
        else:
            print(f"{hero_name} doesn't exist.")


print("Heroes:")
for hero, spells in heroes.items():
    print(f"== {hero}: {', '.join(spells)}")
