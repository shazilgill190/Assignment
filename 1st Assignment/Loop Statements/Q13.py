# Use nested loops to print a pyramid pattern of *.


rows = 5  

for i in range(1, 6):  
    for j in range(rows - i):  
        print(" ", end="")  
    
    for k in range(2 * i - 1):
        print("*", end="")
    print()