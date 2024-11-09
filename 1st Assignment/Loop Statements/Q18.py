# Use a loop to print numbers in reverse order within a given range.

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for number in range(end, start - 1, -1):
    print(number)