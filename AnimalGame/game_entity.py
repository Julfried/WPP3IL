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