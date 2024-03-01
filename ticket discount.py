

user_age = int(input("Enter your age: "))


is_student = input("Are you a student? (yes/no): ").lower()


eligible_for_discount = (user_age <= 12) or (13 <= user_age <= 18 and is_student == 'yes')


if eligible_for_discount:
    print("Congratulations! You are eligible for a discount.")
else:
    print("Sorry, you are not eligible for a discount.")
