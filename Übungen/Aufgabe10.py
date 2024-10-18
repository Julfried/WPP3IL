from Aufgabe1 import get_valid_input

def text2leet(text: str) -> str:
    # Leet dictionary
    LEET = {
        "L": "1",
        "l": "1",
        "E": "3",
        "e": "3",
        "T": "7",
        "t": "7",
        "O": "0",
        "o": "0",
        "S": "5",
        "s": "5",
    }

    # Replace characters with leet characters
    leet_text = ""
    for char in text:
        leet_text += LEET.get(char, char)

    return leet_text

if __name__ == "__main__":
    text = get_valid_input("Text hier eingeben: ")
    leet_text = text2leet(text)
    print(f"Leet text: {leet_text}")