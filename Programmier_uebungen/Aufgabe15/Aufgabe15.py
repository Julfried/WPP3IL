import itertools
import time
from multiprocessing import Pool, cpu_count
from functools import partial
from vignere import vigenere_encrypt, vigenere_decrypt

# Alphabet to use for the brute force attack
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
MAX_CHUNKSIZE = 30000

# Worker function, which does the actual decription task
def brute_force_worker(key, cipher_text, known_plaintext_start):
    # Join key to a single string
    key = "".join(key)

    # Decrpyt the cipher text using the current key
    decrypted_text = vigenere_decrypt(cipher_text, key, known_plaintext_start)

    # Check if the decrypted text starts with the known plaintext start and return
    return (key, decrypted_text) if decrypted_text.startswith(known_plaintext_start) else (None, None)
        

def brute_force_vigenere(cipher_text, known_plaintext_start, max_key_length, terminate_on_first_match=True):
    # Genrate a partial function ==> This way cipher_text and known_plaintext_start are fixed and dont have to be appended for each task
    worker = partial(brute_force_worker,
        cipher_text=cipher_text,
        known_plaintext_start=known_plaintext_start
    )

    # Create a single generator to yield all possible key combinations
    key_combinations = itertools.chain.from_iterable(
        itertools.product(ALPHABET, repeat=key_length) for key_length in range(1, max_key_length + 1)
    )

    # Calculate optimal chunk size
    num_total_combinations = sum([len(ALPHABET) ** key_length for key_length in range(1, max_key_length + 1)])
    print(f"Total number of possible combinations: {num_total_combinations}")
    opt_chucksize = min(num_total_combinations // cpu_count(), MAX_CHUNKSIZE)

    # Perform the brute force attack using multiprocessing
    right_key = None
    right_text = None
    right_step = None
    with Pool(processes=cpu_count()) as pool:
        # Iterate over all possible keys using multiprocessing
        for step, result in enumerate(pool.imap_unordered(worker, key_combinations, chunksize=opt_chucksize), start=1):
            # Get worker results
            key, decrypted_text = result
            right_step = step

            # Terminate the pool if a valid key is found
            if key:
                # Set key for return value
                right_key = key
                right_text = decrypted_text
                right_step = step

                # Terminate the pool if terminate_when_found is set to True
                if terminate_on_first_match:
                    pool.terminate()
                    return right_key, right_text, right_step
            
    return right_key, right_text, right_step

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
    assert decrypted_text == plain_text, "Decryption failed"

    # Step2: Perform brute force attack with early termination
    # Known cipher text and known plaintext start
    cipher_text = "eqvpmtabpb"
    known_plaintext_start = "hello"

    print("\nStep2: Perform brute force attack (max key length = 5) with early termination")
    print(f"Cipher text: {cipher_text}")
    print(f"Known plaintext start: {known_plaintext_start}")

    # Start timer
    start_time = time.time()

    # Perform brute force attack
    key, decrypted_text, step = brute_force_vigenere(
        cipher_text, 
        known_plaintext_start, 
        max_key_length=5, 
        terminate_on_first_match=True
    )

    # End timer
    end_time = time.time()
    # Print results
    if key and decrypted_text:
        print(f"Key found: {key} after {step} steps")
        print(f"Decrypted text: {decrypted_text}")
        print(f"Time taken: {end_time - start_time} seconds")
    
    else:
        print(f"No valid key found. Time taken: {end_time - start_time} seconds")

    # Step3: Perform brute force attack with max key length = 6 with early termination
    print("\nStep3: Perform brute force attack (max key length = 6) with early termination")
    print(f"Cipher text: {cipher_text}")
    print(f"Known plaintext start: {known_plaintext_start}")

    # Start timer
    start_time = time.time()

    # Perform brute force attack
    key, decrypted_text, step = brute_force_vigenere(
        cipher_text, 
        known_plaintext_start, 
        max_key_length=6, 
        terminate_on_first_match=True
    )

    # End timer
    end_time = time.time()
    # Print results
    if key and decrypted_text:
        print(f"Key found: {key} after {step} steps")
        print(f"Decrypted text: {decrypted_text}")
        print(f"Time taken: {end_time - start_time} seconds")
    
    else:
        print(f"No valid key found. Time taken: {end_time - start_time} seconds")

    # Step4: Perform brute force attack with early termination
    # Known cipher text and known plaintext start
    cipher_text = "eqvpmtabpb"
    known_plaintext_start = "hello"

    print("\nStep4: Perform brute force attack (max key length = 5) without early termination")
    print(f"Cipher text: {cipher_text}")
    print(f"Known plaintext start: {known_plaintext_start}")

    # Start timer
    start_time = time.time()

    # Perform brute force attack
    key, decrypted_text, step = brute_force_vigenere(
        cipher_text, 
        known_plaintext_start, 
        max_key_length=5, 
        terminate_on_first_match=False
    )

    # End timer
    end_time = time.time()
    # Print results
    if key and decrypted_text:
        print(f"Key found: {key} after {step} steps")
        print(f"Decrypted text: {decrypted_text}")
        print(f"Time taken: {end_time - start_time} seconds")
    
    else:
        print(f"No valid key found. Time taken: {end_time - start_time} seconds")

    # Step5: Perform brute force attack with max key length = 6 with early termination
    print("\nStep5: Perform brute force attack (max key length = 6) without early termination")
    print(f"Cipher text: {cipher_text}")
    print(f"Known plaintext start: {known_plaintext_start}")

    # Start timer
    start_time = time.time()

    # Perform brute force attack
    key, decrypted_text, step = brute_force_vigenere(
        cipher_text, 
        known_plaintext_start, 
        max_key_length=6, 
        terminate_on_first_match=False
    )

    # End timer
    end_time = time.time()
    # Print results
    if key and decrypted_text:
        print(f"Key found: {key} after {step} steps")
        print(f"Decrypted text: {decrypted_text}")
        print(f"Time taken: {end_time - start_time} seconds")
    
    else:
        print(f"No valid key found. Time taken: {end_time - start_time} seconds")