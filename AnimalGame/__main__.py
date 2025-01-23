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
    animal_classes = {"chicken": Chicken, "cows": Cow, "parrots": Parrot}
    animals = [animal_classes[name]() for name, count in config["Animals"].items() for _ in range(count)]

    # Create a player with name
    player = Player(config["PlayerInfo"]["name"])

    print(animals)

    do_main_loop(player, animals)