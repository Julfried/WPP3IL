from abc import ABC, abstractmethod

class FeedAble(ABC):
    @property
    @abstractmethod
    def noise(self) -> str:
        pass

    def eat(self):
        print(f"{self.__class__.__name__} makes noise while eating: ", self.noise)

class GameEntity:
    def __init__(self, name, health): # constructor
        self.name = name
        self._health = health

    @property
    def health(self):
        return self._health

    def display_info(self):
        print(f"{self.name} has health {self.health}")

class Player(GameEntity):
    def __init__(self, name):
        return super().__init__(name, 20)

class Animal(GameEntity, FeedAble):
    nr_instances = 0
    def __init__(self, health):
        Animal.nr_instances += 1
        super().__init__(f"{Animal.nr_instances}-{self.__class__.__qualname__}", health)

class Cow(Animal):
    def __init__(self):
        super().__init__(10)

    @property
    def noise(self):
        return "Moo"

class Parrot(Animal):
    def __init__(self):
        super().__init__(6)

    @property
    def noise(self):
        return "Squawk"

class Chicken(Animal):
    def __init__(self):
        super().__init__(4)

    @property
    def noise(self):
        return "Cluck"

if __name__ == "__main__":
    entities = [
        Cow(),
        Parrot(),
        Parrot(),
        Chicken(),
        Player("John")
    ]

    for entity in entities:
        if isinstance(entity, FeedAble):
            entity.eat()