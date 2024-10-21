def lauflaengen_encode(input_text:str) -> str:
    # Initialize output and index variable
    output = []
    i = 0
    # Iterate through the input text
    while i < len(input_text):
        # Start at current character ==> counter is 1
        count = 1

        # Count forward until a different character is found
        while i + count < len(input_text) and input_text[i] == input_text[i + count]:
            count += 1

        # Encode the characters if more than 2 consecutive characters are found
        # Else just append the raw characters
        output += [input_text[i] + str(count)] if count > 2 else input_text[i: i + count]

        # Increment index variable by count
        i += count

    return "".join(output)

def lauflaengen_decode(input_text: str) -> str:
    # Initialize output list and index variable
    output = []
    i = 0

    # Iterate through the input text
    while i < len(input_text):
        # Check if the next character is a digit
        if input_text[i + 1].isdigit():
            # Initialize list of digits ==> to also handle numbers with more than one digit
            num_str = []
            j = i + 1

            # Form full numbe from all digits
            while j < len(input_text) and input_text[j].isdigit():
                num_str.append(input_text[j])
                j += 1

            # Convert the collected digits to an integer
            count = int(''.join(num_str))

            # Append to output
            output += [input_text[i]] * count

            # Move index to pos after num ends
            i = j
        else:
            # If no digit follows, just append the character to the output
            output.append(input_text[i])
            i += 1

    return ''.join(output)

if __name__ == "__main__":
    # Test the functions
    text = "ABBCCCKKKKKKK"
    encoded = lauflaengen_encode(text)
    encoded2 = lauflaengen_encode(encoded)

    # Print outputs
    print("Originaler Text:", text)
    print("Encodierter Text:", encoded)
    print("Decodierter Text:", lauflaengen_decode(encoded))
    print("Doppelt Encodierter Text:", encoded2)
    print("\nEncodierter Text == Decodierter Text:", text == lauflaengen_decode(encoded))
    print("\nDoppeltes Encodieren ist nicht sinnvoll, da die Zeichenfolge bereits komprimiert ist und somit keine weiteren Wiederholungen mehr vorkommen können.")