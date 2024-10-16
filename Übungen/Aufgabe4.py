from math import isclose

def get_valid_int_input(prompt):
	while True:
		try:
			return float(input(prompt))
		except ValueError:
			print("Please enter a valid number.")
			

if __name__ == "__main__":
    # Dreieckseiten einlesen
    a = get_valid_int_input("a: ")
    b = get_valid_int_input("b: ")
    c = get_valid_int_input("c: ")
	
    # Check if triangle is valid
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("Dreieck ist gleichseitig")
        elif a == b or a == c or b == c:
            if isclose(a**2 + b**2, c**2) or isclose(a**2 + c**2, b**2) or isclose(b**2 + c**2, a**2):
                print("Dreieck ist rechtwinklig")
            else:
                print("Dreieck ist gleichschenklig")
        else:
            if isclose(a**2 + b**2, c**2) or isclose(a**2 + c**2, b**2) or isclose(b**2 + c**2, a**2):
                print("Dreieck ist rechtwinklig")
            else:
                print("Allgemeines Dreieck")
    else:
        print("Dreieck ist nicht gültig")