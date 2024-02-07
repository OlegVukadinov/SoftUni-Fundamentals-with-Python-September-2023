n = int(input())

for curr_n in range(n):
    text = input()
    name = text.split("@")[1].split("|")[0]
    age = text.split("#")[1].split("*")[0]

    print(f"{name} is {age} years old.")