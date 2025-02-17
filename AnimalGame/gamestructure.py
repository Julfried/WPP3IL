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

class Animal(GameEntity, FeedAble):
    nr_instances = 0
    def __init__(self, health):
        Animal.nr_instances += 1
        super().__init__(f"{Animal.nr_instances}-{self.__class__.__qualname__}", health)

class Player(GameEntity):
    def __init__(self, name):
        return super().__init__(name, 20)
    
    def feed(self, animal: Animal):
        print(f"{self.name} fed {animal.name}")
        animal.eat()
