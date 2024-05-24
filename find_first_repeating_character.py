def find_first_repeating_character(s):
    # Dictionary to store the count of characters
    char_count = {}
    
    # Iterate through each character in the string
    for char in s:
        if char in char_count:
            # Character found for the second time
            print(f"First repeating character: {char}")
            print(f"Memory address of '{char}': {id(char)}")
            return char
        else:
            # Add character to the dictionary
            char_count[char] = 1
    
    # No repeating character found
    print("No repeating character found")
    return None

# Testing the function
print(find_first_repeating_character("hello"))  # Expected output: 'l' and its memory address
print(find_first_repeating_character("abcd"))   # Expected output: None
print(find_first_repeating_character("aab"))    # Expected output: 'a' and its memory address
