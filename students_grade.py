num= int(input("Enter the total no of students"))
i=1
while i <= num:
    total_grade=0
    num=int(input(f"Ënter tho total no of subject for students {i}:"))

    for j in range (1, num+1):
        grade=float(input("entersubject{j} grade for student {i}"))
        total_grade += grade
    
    average_grade=total_grade/ num
    print(f"Average grade for student {i}: {average_grade: .2f}")
    i += 1
