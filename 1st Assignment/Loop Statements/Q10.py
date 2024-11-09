# Use a loop to count the number of digits in an integer.

n=int(input("Enter Your Integer:"))
count=0

for digit in str(abs(n)):
    count+=1
    
print("Your Total Number Is:",count)
