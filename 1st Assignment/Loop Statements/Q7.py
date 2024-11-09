# Find the factorial of a number using a while loop.

n = int(input("Enter a number: "))  
fac = 1  
i = 1  

while i <= n:
    fac *= i  
    i += 1  

print("The factorial of", n, "is:", fac)