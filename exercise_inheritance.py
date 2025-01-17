class GameEntity:
    def __init__(self, name, health): # constructor
        self.name = name
        self._health = health

    @property
    def health(self):
        return self._health

    def display_info(self):
        print(f"{self.name} has health {self.health}")

class Animal(GameEntity):
    nr_instances = 0
    def __init__(self, health):
        Animal.nr_instances += 1
        super().__init__(f"{Animal.nr_instances}-{self.__class__.__qualname__}", health)
    
class Cow(Animal):
    def __init__(self):
        super().__init__(10)

class Parrot(Animal):
    def __init__(self):
        super().__init__(6)

class Chicken(Animal):
    def __init__(self):
        super().__init__(4)

if __name__ == "__main__":
    animals = [
        Cow(),
        Parrot(),
        Parrot(),
        Chicken(),
    ]

    for animal in animals:
        animal.display_info()