from typing import TypeVar, Type

T = TypeVar('T')

def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

from typing import Callable

def get_valid_input(prompt, cast_to = float):
	while True:
		try:
			casted: Type[cast_to] = cast_to(input(prompt))
			return casted
		except ValueError:
			print("Please enter a valid number.")

if __name__ == "__main__":
    fahrenheit = get_valid_input("Insert temperature in Fahrenheit: ")
    celsius = convert_fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is {celsius}°C")