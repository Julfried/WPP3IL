from .game_entity import GameEntity
from .animals import Animal

class Player(GameEntity):
    def __init__(self, name):
        return super().__init__(name, 20)
    
    def feed(self, animal: Animal):
        print(f"{self.name} fed {animal.name}")
        animal.eat()