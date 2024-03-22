def reverse_string(s):
    # Base case: If the string is empty or contains only one character, return it as is
    if len(s) <= 1:
        return s
    else:
        # Recursive case: Separate the first character from the remaining characters
        first_char = s[0]
        remaining_chars = s[1:]
        # Recursively call reverse_string on the remaining characters
        reversed_remaining = reverse_string(remaining_chars)
        # Append the first character to the reversed remaining string
        return reversed_remaining + first_char

# Example usage
input_string = "hello"
reversed_result = reverse_string(input_string)
print(f"Reversed string for '{input_string}': {reversed_result}")
