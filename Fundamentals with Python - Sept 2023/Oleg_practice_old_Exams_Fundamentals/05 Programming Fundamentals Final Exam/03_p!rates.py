cities = {}
while True:
    command = input()
    if command == "Sail":
        break

    towns = command.split("||")
    city = towns[0]
    population = int(towns[1])
    gold = int(towns[2])

    if city not in cities.keys():
        cities[city] = {"population": 0, "gold": 0}
    cities[city]["population"] += population
    cities[city]["gold"] += gold

while True:
    command = input()
    if command == "End":
        break
    events = command.split("=>")
    action = events[0]

    if action == "Plunder":
        town = events[1]
        people = int(events[2])
        gold = int(events[3])
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        cities[town]["population"] -= people
        cities[town]["gold"] -= gold

        if cities[town]["population"] == 0 or cities[town]["gold"] == 0:
            cities.pop(town)
            print(f"{town} has been wiped off the map!")

    elif action == "Prosper":
        town = events[1]
        gold = int(events[2])

        if gold < 0:
            print(f"Gold added cannot be a negative number!")

        else:
            cities[town]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")
if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for town, town_information in cities.items():
        print(f"{town} -> Population: {town_information['population']} citizens, Gold: {town_information['gold']} kg")

else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")