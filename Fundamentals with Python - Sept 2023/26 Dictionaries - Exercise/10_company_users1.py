users_dict = {}
while True:
    data = input()
    if data == "End":
        break

    info = data.split(" -> ")
    name = info[0]
    id = info[1]

    if name not in users_dict.keys():
        users_dict[name] = []
        users_dict[name].append(id)
    elif name in users_dict.keys():
        if id not in users_dict[name]:
           users_dict[name].append(id)

for name, id in users_dict.items():
    print(f"{name}")
    for curr_id in id:
        print(f"-- {curr_id}")