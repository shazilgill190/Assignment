# Ask the user for a grade percentage and display the corresponding letter grade (A, B, C, D, F).


Marks = float(input("Enter your Marks: "))


if Marks >= 90:
    print("Your grade is: A")
elif Marks >= 80:
    print("Your grade is: B")
elif Marks >= 70:
    print("Your grade is: C")
elif Marks >= 60:
    print("Your grade is: D")
else:
    print("Your grade is: F")
