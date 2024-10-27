import itertools
import time
from vignere import vigenere_encrypt, vigenere_decrypt

def brute_force_vigenere(cipher_text, known_plaintext_start, max_key_length=5):
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

    # Iterate over all possible key lengths
    for key_length in range(1, max_key_length + 1):
        # Generate all possible keys and iterate over them
        for key in itertools.product(ALPHABET, repeat=key_length):
            key = "".join(key)
            # Decrypt the cipher text using the key
            decrypted_text = vigenere_decrypt(cipher_text, key)
            # Check if the decrypted text starts with the known plaintext
            if decrypted_text.startswith(known_plaintext_start):
                return key, decrypted_text
    return None, None

if __name__ == "__main__":
    # Step1: Valdiate the cypther and decypher functions
    # Define plain text and print
    plain_text = 'test'
    key = 'key'

    print("Step1: Validate the cypther and decypher functions")
    print(f"Plain text: {plain_text}")

    # Encrypt the plain text
    cipher_text = vigenere_encrypt(plain_text, key)

    # Print the cipher text
    print(f"Cipher text: {cipher_text}")

    # Validate the functions
    decrypted_text = vigenere_decrypt(cipher_text, key)
    print(f"Decrypted text: {decrypted_text}")

    # Step2: Perform brute force attack
    # Known cipher text and known plaintext start
    cipher_text = "eqvpmtabpb"
    known_plaintext_start = "hello"

    print("\nStep2: Perform brute force attack (max key length = 5)")
    print(f"Cipher text: {cipher_text}")
    print(f"Known plaintext start: {known_plaintext_start}")

    # Start timer
    start_time = time.time()

    # Perform brute force attack
    key, decrypted_text = brute_force_vigenere(cipher_text, known_plaintext_start)

    # End timer
    end_time = time.time()
    # Print results
    if key and decrypted_text:
        print(f"Key found: {key}")
        print(f"Decrypted text: {decrypted_text}")
        print(f"Time taken: {end_time - start_time} seconds")
    
    else:
        print(f"No valid key found. Time taken: {end_time - start_time} seconds")

    # Step3: Perform brute force attack with max key length = 6
    print("\nStep3: Perform brute force attack (max key length = 6)")
    print(f"Cipher text: {cipher_text}")
    print(f"Known plaintext start: {known_plaintext_start}")

    # Start timer
    start_time = time.time()

    # Perform brute force attack
    key, decrypted_text = brute_force_vigenere(cipher_text, known_plaintext_start, max_key_length=6)

    # End timer
    end_time = time.time()
    # Print results
    if key and decrypted_text:
        print(f"Key found: {key}")
        print(f"Decrypted text: {decrypted_text}")
        print(f"Time taken: {end_time - start_time} seconds")
    
    else:
        print(f"No valid key found. Time taken: {end_time - start_time} seconds")