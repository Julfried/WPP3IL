def vigenere_encrypt(plain_text, key):
    # Initialize the cipher text
    cipher_text = ''
    # Initialize the key index
    key_index = 0
    # Iterate over the plain text
    for char in plain_text:
        # Check if the character is a letter
        if char.isalpha():
            # Calculate the shift value
            shift = ord(key[key_index].lower()) - ord('a')
            # Encrypt the character
            cipher_text += chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
            # Update the key index
            key_index = (key_index + 1) % len(key)
        else:
            # Append the character to the cipher text
            cipher_text += char
    # Return the cipher text
    return cipher_text

def vigenere_decrypt(cipher_text, key, length_to_decrypt=None):
    # Initialize the plain text
    plain_text = ''
    # Initialize the key index
    key_index = 0
    # Iterate over the cipher text
    for char in cipher_text:
        # Check if the character is a letter
        if char.isalpha():
            # Calculate the shift value
            shift = ord(key[key_index].lower()) - ord('a')
            # Decrypt the character
            plain_text += chr((ord(char.lower()) - ord('a') - shift) % 26 + ord('a'))
            # Update the key index
            key_index = (key_index + 1) % len(key)
        else:
            # Append the character to the plain text
            plain_text += char
    # Return the plain text
    return plain_text