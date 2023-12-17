list_of_integers = input().split() # в списъка това всъщност са стрингове
number_n = int(input())

for i in range(len(list_of_integers)):       # превръщаме списъка със стринговете в списък с интеджери
    list_of_integers[i] = int(list_of_integers[i])

for current_number in range(1, number_n + 1):
    list_of_integers.remove(min(list_of_integers))

for i in range(len(list_of_integers)):       # превръщаме списъка с интеджери в списък със стрингове
    list_of_integers[i] = str(list_of_integers[i])

print(", ".join(list_of_integers))


