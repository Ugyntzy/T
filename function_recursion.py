def sum_of_digits(n):
    # Base case: if n is 0, the sum of its digits is 0
    if n == 0:
        return 0
    else:
        # Recursive case: last digit + sum of the digits of the remaining number
        last_digit = n % 10
        remaining_number = n // 10
        return last_digit + sum_of_digits(remaining_number)

# Testing the function
print(sum_of_digits(123))  # Output: 6
print(sum_of_digits(9876))  # Output: 30
