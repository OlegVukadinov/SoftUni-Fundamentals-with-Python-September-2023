age = int(input())

if age <= 14:
    drink = "toddy"
    print("drink toddy")
elif 15 < age <= 18:
    drink = "coke"
    print("drink coke")
elif 19 < age <= 21:
    drink = "beer"
    print("drink beer")
elif 21 < age:
    drink = "whisky"
    print("drink whisky")