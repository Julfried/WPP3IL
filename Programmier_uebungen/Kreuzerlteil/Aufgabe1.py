from typing import TypeVar, Callable

T = TypeVar('T')

def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def get_valid_input(prompt: str, cast_to: Callable[[str], T] = str) -> T:
    while True:
        try:
            return cast_to(input(prompt))
        except ValueError:
            if cast_to == int:
                print("Please enter a valid integer.")
            elif cast_to == float:
                print("Please enter a valid float.")
            elif cast_to == str:
                print("Please enter a valid string.")
            else:
                print("Invalid input. Please try again.")

if __name__ == "__main__":
    fahrenheit = get_valid_input("Insert temperature in Fahrenheit: ", cast_to=float)
    celsius = convert_fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is {celsius}°C")