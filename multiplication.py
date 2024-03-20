def generate_multiplication_table(number, limit):
    print(f"Multiplication table for {number} up to {limit}:")

    for i in range(1, limit + 1):
        result = number * i
        print(f"{number} x {i} = {result}")

def main():
    try:
        number = int(input("Enter the number for the multiplication table: "))
        limit = int(input("Enter the limit for the table: "))

        if limit <= 0:
            print("Please enter a positive limit.")
        else:
            generate_multiplication_table(number, limit)
    except ValueError:
        print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main()
