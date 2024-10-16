def get_valid_int_input(prompt):
	while True:
		try:
			return int(input(prompt))
		except ValueError:
			print("Please enter a valid number.")
			
if __name__ == "__main__":
    n = get_valid_int_input("n: ")

    match n:
        case 1: print("Montag")
        case 2: print("Dienstag")
        case 3 : print("Mittwoch")
        case 4 : print("Donnerstag")
        case 5 : print("Freitag")
        case 6 : print("Samstag")
        case 7 : print("Sonntag")
        case _ : raise ValueError("n must be between 1 and 7")
