population_list = list(map(int, input().split(", ")))
min_wealth = int(input())

for curr_index in range(len(population_list)):
    if population_list[curr_index] < min_wealth:
        diff = min_wealth - population_list[curr_index]
        max_number = max(population_list)

        if max_number - diff >= min_wealth:
            population_list[population_list.index(max_number)] -= diff
            population_list[curr_index] += diff
if sum(population_list) >= len(population_list) * min_wealth:
    print(population_list)
else:
    print("No equal distribution possible")