number_of_commands = int(input())

parking = {}

for curr_n in range(1,number_of_commands + 1):
    command = input().split()

    if command[0] == "register":
        username = command[1]
        license_plate_number = command[2]
        if username in parking:
            print(f"ERROR: already registered with plate number {parking[username]}")
        else:
            parking[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully") ########

    elif command[0] == "unregister":
        username = command[1]
        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking[username]
for username, license_plate_number in parking.items():
    print(f"{username} => {license_plate_number}")