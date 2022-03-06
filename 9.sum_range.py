# Print sum of the nos within a range
low = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

sum = 0

while low<=upper:
    sum+=low
    low+=1

print(f"Sum is {sum}")
