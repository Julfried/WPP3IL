from Aufgabe1 import get_valid_input

def convert_seconds_to_string(seconds):
    hours = seconds // 3600
    seconds = seconds % 3600
    minutes = seconds // 60
    seconds = seconds % 60
    return "{}:{}:{}".format(hours, minutes, seconds)

if __name__ == "__main__":
    # test with input 1234
    seconds = 1234
    time = convert_seconds_to_string(seconds)
    print(time)

    seconds = get_valid_input("Insert seconds: ", cast_to=int)
    time = convert_seconds_to_string(seconds)
    print(time)