from abc import ABC, abstractmethod

class DeathStar(ABC):
    has_reactor_core = True

    @abstractmethod
    def fire(self):
        pass

class StarKillerBase(DeathStar):
    def fire(self):
        print("Firing the Starkiller Base")

if __name__ == "__main__":
    star_killer = StarKillerBase()
    star_killer.fire()
    print(star_killer.has_reactor_core) 