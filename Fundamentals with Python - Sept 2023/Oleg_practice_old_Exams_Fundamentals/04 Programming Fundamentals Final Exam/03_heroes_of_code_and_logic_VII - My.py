number_heroes = int(input())
heroes = {}

for curr_num in range(number_heroes):
    hero_info = input().split(" ")
    hero_name, hit_points, mana_points = hero_info[0], int(hero_info[1]), int(hero_info[2]),
    heroes[hero_name] = {"hit_points": hit_points, "mana_points": mana_points}

while True:
    command = input()
    if command == "End":
        break
    com = command.split(" - ")
    action = com[0]

    if action == "CastSpell":
        hero_name = com[1]
        MP_needed = int(com[2])
        spell_name = com[3]
        if heroes[hero_name]["mana_points"] >= MP_needed:
            heroes[hero_name]["mana_points"] -= MP_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['mana_points']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif action == "TakeDamage":
        hero_name = com[1]
        damage = int(com[2])
        attacker = com[3]
        heroes[hero_name]['hit_points'] -= damage
        if heroes[hero_name]["hit_points"] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['hit_points']} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del heroes[hero_name]
    elif action == "Recharge":
        hero_name = com[1]
        amount = int(com[2])
        if heroes[hero_name]['mana_points'] + amount > 200:
            amount = 200 - heroes[hero_name]['mana_points']
            heroes[hero_name]['mana_points'] = 200
        else:
            heroes[hero_name]['mana_points'] += amount
        print(f"{hero_name} recharged for {amount} MP!")

    elif action == "Heal":
        hero_name = com[1]
        amount = int(com[2])
        if heroes[hero_name]['hit_points'] + amount > 100:
            amount = 100 - heroes[hero_name]['hit_points']
            heroes[hero_name]['hit_points'] = 100
        else:
            heroes[hero_name]['hit_points'] += amount
        print(f"{hero_name} healed for {amount} HP!")

for hero_name, stats in heroes.items():
    print(f"{hero_name}")
    print(f"  HP: {stats['hit_points']}")
    print(f"  MP: {stats['mana_points']}")

