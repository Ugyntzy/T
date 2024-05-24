# force.py

# Step a: Print the header and border line
print("Force Calculation Program")
print("-------------------------")

# Step b: Prompt the user to select the missing value
print("Select the missing value to calculate:")
print("1. Mass (m)")
print("2. Acceleration (a)")
print("3. Force (F)")

missing_value_choice = input("Enter the option number (1, 2, or 3): ")

# Step c: Based on the user's input, calculate the missing value
if missing_value_choice == '1':
    # Calculate mass (m)
    a = float(input("Enter acceleration (a): "))
    F = float(input("Enter force (F): "))
    if a != 0:
        m = F / a
        print(f"The calculated mass (m) is: {m}")
    else:
        print("Acceleration cannot be zero.")
elif missing_value_choice == '2':
    # Calculate acceleration (a)
    m = float(input("Enter mass (m): "))
    F = float(input("Enter force (F): "))
    if m != 0:
        a = F / m
        print(f"The calculated acceleration (a) is: {a}")
    else:
        print("Mass cannot be zero.")
elif missing_value_choice == '3':
    # Calculate force (F)
    m = float(input("Enter mass (m): "))
    a = float(input("Enter acceleration (a): "))
    F = m * a
    print(f"The calculated force (F) is: {F}")
else:
    print("Invalid option. Please select 1, 2, or 3.")
