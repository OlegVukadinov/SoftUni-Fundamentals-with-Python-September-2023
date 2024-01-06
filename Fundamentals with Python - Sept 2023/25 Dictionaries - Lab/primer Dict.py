info = input().split()

my_dict = {}

for i in range(0, len(info), 2): # създаваме и пълним речника my_dict
    key = info[i]
    value = info[i + 1]
    my_dict[key] = int(value)

for k in my_dict.keys(): # печатаме ключовете на един ред
    print(k, end = " ")

for v in my_dict.values(): # печатаме values на един ред с end=" "
    print(v, end=" ")

    # примерен вход  bread 10 butter 4 sugar 9 jam 12