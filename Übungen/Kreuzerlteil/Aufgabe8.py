from Aufgabe1 import get_valid_input

number = get_valid_input("Zahl: ", cast_to=int)

print("Ziffernsummee:", sum([int(i) for i in str(number)]))