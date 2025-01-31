from .game_entity import GameEntity, FeedAble

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