n = int(input())

cars = {}

for _ in range(n):
    car_info = input().split("|")
    car, mileage, fuel = car_info[0], int(car_info[1]), int(car_info[2])
    cars[car] = {"mileage": mileage, "fuel": fuel}

while True:
    command = input()
    if command == "Stop":
        break
    command_parts = command.split(" : ")
    action = command_parts[0]
    car = command_parts[1]

    if action == "Drive":
        distance, required_fuel = int(command_parts[2]), int(command_parts[3])

        if cars[car]["fuel"] < required_fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car]["mileage"] += distance
            cars[car]["fuel"] -= required_fuel
            print(f"{car} driven for {distance} kilometers. {required_fuel} liters of fuel consumed.")

            if cars[car]["mileage"] >= 100000:
                del cars[car]
                print(f"Time to sell the {car}!")

    elif action == "Refuel":
        refuel_amount = int(command_parts[2])
        current_fuel = cars[car]["fuel"]

        if current_fuel + refuel_amount > 75:
            refuel_amount = 75 - current_fuel

        cars[car]["fuel"] += refuel_amount
        print(f"{car} refueled with {refuel_amount} liters")

    elif action == "Revert":
        kilometers = int(command_parts[2])
        cars[car]["mileage"] -= kilometers

        if cars[car]["mileage"] < 10000:
            cars[car]["mileage"] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")


for car, stats in cars.items():
    print(f"{car} -> Mileage: {stats['mileage']} kms, Fuel in the tank: {stats['fuel']} lt.")
