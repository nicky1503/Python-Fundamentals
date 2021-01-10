class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.birds = []
        self.fishes = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'bird':
            self.birds.append(name)
        elif species == 'fish':
            self.fishes.append(name)

    def got_info(self, species, total_animals):
        if species == 'mammal':
            print(f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}")
            print(f"Total animals: {total_animals}")
        elif species == 'bird':
            print(f"Birds in {self.zoo_name}: {', '.join(self.birds)}")
            print(f"Total animals: {total_animals}")
        elif species == 'fish':
            print(f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}")
            print(f"Total animals: {total_animals}")


name_of_zoo = input()
zoo_park = Zoo(name_of_zoo)
num_of_animals = int(input())
for a in range(num_of_animals):
    species, name = input().split()
    zoo_park.add_animal(species, name)
kind_of_animal = input()
zoo_park.got_info(kind_of_animal, num_of_animals)



