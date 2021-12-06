# Write a program to print factorial of an inputted number using for loop
n = int(input("Enter the number: "))
fact = 1;

for i in range(1, n+1):
    fact*=i

print(fact)
