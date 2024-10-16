def get_valid_int_input(prompt):
	while True:
		try:
			return int(input(prompt))
		except ValueError:
			print("Please enter a valid number.")

def convert_seconds_to_string(seconds):
    hours = int(seconds // 3600)
    seconds = seconds % 3600
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return "{}:{}:{}".format(hours, minutes, seconds)

if __name__ == "__main__":
    # test with input 1234
    seconds = 1234
    time = convert_seconds_to_string(seconds)
    print(time)

    seconds = get_valid_int_input("Insert seconds: ")
    time = convert_seconds_to_string(seconds)
    print(time)