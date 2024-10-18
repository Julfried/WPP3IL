from Aufgabe1 import get_valid_input

def isAnangram(s1:str, s2:str) -> bool:
    set_s1 = set([char for char in s1.lower().replace(" ", "")])
    set_s2 = set([char for char in s2.lower().replace(" ", "")])
    return set_s1 == set_s2

if __name__ == "__main__":
    s1 = get_valid_input("String 1: ")
    s2 = get_valid_input("String 2: ")
    print("Anagram" if isAnangram(s1, s2) else "Kein Anagram")