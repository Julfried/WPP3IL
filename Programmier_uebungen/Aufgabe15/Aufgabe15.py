import itertools
import time
from multiprocessing import Pool, cpu_count
from functools import partial
from vignere import vigenere_encrypt, vigenere_decrypt

# Alphabet to use for the brute force attack
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

# Worker function, which does the actual decription task
def brute_force_worker(key, cipher_text, known_plaintext_start):
    key = "".join(key)
    # Decrypt the cipher text using the key
    decrypted_text = vigenere_decrypt(cipher_text, key)

    # Check if the decrypted text starts with the known plaintext
    if decrypted_text.startswith(known_plaintext_start):
        return key, decrypted_text
    
    else:
        return None, None

def brute_force_vigenere(cipher_text, known_plaintext_start, max_key_length=5):
    # Genrate a partial function ==> This way cipher_text and known_plaintext_start are fixed and dont have to be appended for each task
    worker = partial(brute_force_worker,
        cipher_text=cipher_text,
        known_plaintext_start=known_plaintext_start 
    )

    # Perform the brute force attack using multiprocessing
    with Pool(processes=cpu_count()) as pool:
        # Iterate over all possible key lengths
        for key_length in range(1, max_key_length + 1):
            # Generate all possible keys
            key_combinations = itertools.product(ALPHABET, repeat=key_length)

            # Callculate optimal chunksize
            opt_chucksize = min(len(ALPHABET) ** key_length // cpu_count(), 100000)

            # Iterate over all possible keys using multiprocessing
            for result in pool.imap_unordered(worker, key_combinations, chunksize=opt_chucksize):
                key, decrypted_text = result

                if key:
                    pool.terminate() # Terminate the pool if a valid key is found
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