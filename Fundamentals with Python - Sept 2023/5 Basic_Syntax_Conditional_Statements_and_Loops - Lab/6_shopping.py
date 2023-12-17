budget = int(input())
counter_budget = 0
command = input()

while command != "End":
    price = int(command)

    counter_budget += price

    if counter_budget > budget:
        print("You went in overdraft!")
        break

    command = input()
else:
    print("You bought everything needed.")
