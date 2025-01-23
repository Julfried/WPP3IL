import tomllib
from .player import Player
from .animals import Chicken, Cow, Parrot, Animal

# Main game loop
def do_main_loop(player: Player, animals: list[Animal]):
    for animal in animals:
        player.feed(animal)
        animal.display_info()

if __name__ == "__main__":
    with open("config.toml", mode="rb") as fp:
        config = tomllib.load(fp)

    # Setup game
    animals = []
    for name, count in config["Animals"].items():
        match name:
            case "chicken":
                for _ in range(count):
                    animals.append(Chicken())
            case "cow":
                for _ in range(count):
                    animals.append(Cow())
            case "parrot":
                for _ in range(count):
                    animals.append(Parrot())

    # Create a player with name
    player = Player(config["PlayerInfo"]["name"])

    print(animals)

    do_main_loop(player, animals)