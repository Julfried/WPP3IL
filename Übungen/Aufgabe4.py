from math import isclose
from Aufgabe1 import get_valid_input

if __name__ == "__main__":
    # Dreieckseiten einlesen
    a = get_valid_input("a: ", cast_to=float)
    b = get_valid_input("b: ", cast_to=float)
    c = get_valid_input("c: ", cast_to=float)
	
    # Check if triangle is valid
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("Dreieck ist gleichseitig")
        elif a == b or a == c or b == c:
            if isclose(a**2 + b**2, c**2) or isclose(a**2 + c**2, b**2) or isclose(b**2 + c**2, a**2):
                print("Dreieck ist rechtwinklig und gleichschenklig")
            else:
                print("Dreieck ist gleichschenklig")
        else:
            if isclose(a**2 + b**2, c**2) or isclose(a**2 + c**2, b**2) or isclose(b**2 + c**2, a**2):
                print("Dreieck ist rechtwinklig")
            else:
                print("Allgemeines Dreieck")
    else:
        print("Dreieck ist nicht gültig")