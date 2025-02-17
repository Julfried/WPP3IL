from ..gamestructure import Animal

class Wolf(Animal):
    def __init__(self):
        super().__init__(8)

    @property
    def noise(self):
        return "NomNom"
    
    def attack(self, animal: Animal):
        animal.health -= 10
        print(f"{self.name} attacked {animal.name}")

        if animal.health <= 0:
            print(f"{animal.name} died")
        
            if(not isinstance(animal, Wolf)):
                self.eat()
            del animal