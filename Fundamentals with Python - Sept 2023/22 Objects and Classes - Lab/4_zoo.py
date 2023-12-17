class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1
    def get_info(self, species):
        self.species = species
        string_to_print = ""

        if species == "mammal":
            string_to_print += f"Mammals in {self.name}: {', '.join(self.mammals)}"
        if species == "fish":
            string_to_print += f"Fishes in {self.name}: {', '.join(self.fishes)}"
        if species == "bird":
            string_to_print += f"Birds in {self.name}: {', '.join(self.birds)}"

        string_to_print += f"\nTotal animals: {Zoo.__animals}"
        return string_to_print

zoo_name = input()
zoo_objects = Zoo(zoo_name)
counter_animals= int(input())

for curr_animal in range(counter_animals):
     animal = input().split(" ")
     species = animal[0]
     name = animal[1]
     zoo_objects.add_animal(species, name)

searched_species = input()
print(zoo_objects.get_info(searched_species))
