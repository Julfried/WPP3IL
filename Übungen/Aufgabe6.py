from Aufgabe1 import get_valid_input

def date_is_valid(tag, monat, jahr):
    if is_schaltjahr(jahr):
        valid_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        valid_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if jahr < 0:
        return False
    
    if monat < 1 or monat > 12:
        return False
    
    if tag < 1 or tag > valid_days[monat - 1]:
        return False
    
    return True

def is_schaltjahr(jahr):
    if jahr % 4 == 0 and (jahr % 100 == 0 or jahr % 400 != 0):
        return True
    return False

if __name__ == "__main__":
    tag = get_valid_input("Tag: ", cast_to=int)
    monat = get_valid_input("Monat: ", cast_to=int)
    jahr = get_valid_input("Jahr: ", cast_to=int)

    # Check if the date is valid
    if not date_is_valid(tag, monat, jahr):
        print(f"Datum {tag}.{monat}.{jahr} nicht gültig.")
    else:
        if is_schaltjahr(jahr):
            print(f"{jahr} ist ein Schaltjahr.")
        else:
            print(f"{jahr} ist kein Schaltjahr.")