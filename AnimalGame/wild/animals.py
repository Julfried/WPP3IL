from ..gamestructure import Animal

class Wolf(Animal):
    def __init__(self):
        super().__init__(8)

    @property
    def noise(self):
        return "NomNom"