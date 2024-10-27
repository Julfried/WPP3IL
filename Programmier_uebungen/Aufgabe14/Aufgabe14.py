
def mult_manu(num_a, num_b):
    # Convert numbers to strings
    str_a = str(num_a)
    str_b = str(num_b)

    # List to store all intermediate results
    intermediate_results = []
    
    # Manual multiplication
    for digit_b in str_b:
        intermediate_result = int(digit_b) * num_a
        intermediate_results.append(intermediate_result)

    # Calculate the final result
    final_res = num_a * num_b
    
    # Format output
    print(f"{num_a} * {num_b}")
    underscore = "-" * (len(str_a) + len(str_b) + 3)
    print(underscore)
    for i, result in enumerate(intermediate_results):
        result_string =  " " * i + str(result) if i != 0 else str(result)
        print(result_string)
    print(underscore)
    print(final_res)

if __name__ == "__main__":
    # Example 1
    mult_manu(123, 456)

    # Example 2
    print("\n\n")
    mult_manu(100024, 655457)