from Aufgabe1 import get_valid_input
			
if __name__ == "__main__":
    n = get_valid_input("n: ", cast_to=int)

    match n:
        case 1: print("Montag")
        case 2: print("Dienstag")
        case 3 : print("Mittwoch")
        case 4 : print("Donnerstag")
        case 5 : print("Freitag")
        case 6 : print("Samstag")
        case 7 : print("Sonntag")
        case _ : raise ValueError("n must be between 1 and 7")