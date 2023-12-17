from collections import defaultdict
n = int(input())
# Initialize dictionaries to store dragon data and type statistics
dragons = defaultdict(dict)
type_stats = defaultdict(lambda: {"damage": 0, "health": 0, "armor": 0, "count": 0})

# Read the number of dragons


# Process input and update dragon data and type statistics
for _ in range(n):
    data = input().split()
    dragon_type, dragon_name, damage, health, armor = data[0], data[1], data[2], data[3], data[4]

    # Assign default values to missing stats
    if damage == "null":
        damage = 45
    else:
        damage = int(damage)

    if health == "null":
        health = 250
    else:
        health = int(health)

    if armor == "null":
        armor = 10
    else:
        armor = int(armor)

    # Update the dragon data
    dragons[(dragon_type, dragon_name)] = {"damage": damage, "health": health, "armor": armor}

    # Update the type statistics
    type_stats[dragon_type]["damage"] += damage
    type_stats[dragon_type]["health"] += health
    type_stats[dragon_type]["armor"] += armor
    type_stats[dragon_type]["count"] += 1

# Sort dragons by name and type
sorted_dragons = sorted(dragons.keys(), key=lambda x: (x[0], x[1]))

# Print the aggregated data


# Print type statistics
for dragon_type, stats in type_stats.items():
    count = stats["count"]
    avg_damage = stats["damage"] / count
    avg_health = stats["health"] / count
    avg_armor = stats["armor"] / count
    print(f"{dragon_type}::({avg_damage:.2f}/{avg_health:.2f}/{avg_armor:.2f})")
    for dragon_type, dragon_name in sorted_dragons:
        data = dragons[(dragon_type, dragon_name)]
        print(f"-{dragon_name} -> damage: {data['damage']}, health: {data['health']}, armor: {data['armor']}")
