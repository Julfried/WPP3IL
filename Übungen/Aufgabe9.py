from Aufgabe1 import get_valid_input

def dez2bin(dez):
    bin = []
    while dez > 0:
        bin = [dez % 2] + bin
        dez = dez // 2
    return bin


if __name__ == "__main__":
    # Einlesen
    int = get_valid_input("Bitte geben Sie eine Dezimalzahl ein: ", cast_to=int)

    # Umrechnen dezinmal zu binär
    bin = dez2bin(int)

    # Liste umdrehen
    bin.reverse()

    # Ausgabe
    print(f"Die Zahl {int} entspricht der Menge: ", 
          "{", ", ".join([str(i) for i, data in enumerate(bin) if data ==1]), "}"
    )
    