import time
import itertools

from vignere import vigenere_encrypt, vigenere_decrypt

if __name__ == '__main__':
    plain_text = 'Hello, World!'
    key = 'key'

    print(f"Plain text: {plain_text}")

    # Encrypt the plain text
    cipher_text = vigenere_encrypt(plain_text, key)

    # Print the cipher text
    print(f"Cipher text: {cipher_text}")

    def brute_force_vigenere(cipher_text, known_plaintext_start):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        max_key_length = 5

        start_time = time.time()

        for key_length in range(1, max_key_length + 1):
            for key_tuple in itertools.product(alphabet, repeat=key_length):
                key = ''.join(key_tuple)
                decrypted_text = vigenere_decrypt(cipher_text, key)
                if decrypted_text.startswith(known_plaintext_start):
                    end_time = time.time()
                    print(f"Key found: {key}")
                    print(f"Decrypted text: {decrypted_text}")
                    print(f"Time taken: {end_time - start_time} seconds")
                    return key, decrypted_text

        end_time = time.time()
        print(f"No valid key found. Time taken: {end_time - start_time} seconds")
        return None, None

    # Known cipher text and known plaintext start
    cipher_text = "eqvpmtabpb"
    known_plaintext_start = "hallo"

    # Perform brute force attack
    key, decrypted_text = brute_force_vigenere(cipher_text, known_plaintext_start)
