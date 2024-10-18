from typing import TypeVar, Callable

T = TypeVar('T')

def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def get_valid_input(prompt: str, cast_to: Callable[[str], T] = str) -> T:
    while True:
        try:
            return cast_to(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    fahrenheit = get_valid_input("Insert temperature in Fahrenheit: ", cast_to=float)
    celsius = convert_fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is {celsius}°C")