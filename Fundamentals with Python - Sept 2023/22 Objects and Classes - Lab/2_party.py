class Party:
    people = []

    def __init__(self, people):
        self.people = people

    while True:
        command = input()
        if command == "End":
            print(f"Going: {', '.join(people)}")
            print(f"Total: {len(people)}")
            break
        else:
            people.append(command)
