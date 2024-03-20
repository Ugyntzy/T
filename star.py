def generate_right_triangle(height):
    for i in range(1, height + 1):
        print("*" * i)

def main():
    try:
        height = int(input("Enter the height of the right triangle: "))
        if height <= 0:
            print("Please enter a positive height.")
        else:
            generate_right_triangle(height)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
