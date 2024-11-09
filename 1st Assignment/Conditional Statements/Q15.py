# Write a program to check if a number is within a specified range


number = float(input("Enter a number: "))
lower_limit = float(input("Enter the lower limit of the range: "))
upper_limit = float(input("Enter the upper limit of the range: "))

if lower_limit <= number <= upper_limit:
    print(number, "is within the range", lower_limit, "to", upper_limit)
else:
    print(number, "is outside the range", lower_limit, "to", upper_limit)