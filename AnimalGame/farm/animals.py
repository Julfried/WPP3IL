from ..gamestructure import Animal

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