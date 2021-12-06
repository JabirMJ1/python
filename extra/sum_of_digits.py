# print sum of digits of an i/p number
n = int(input("Enter the number: "))

sum=0

while n>0:
    last_digit = n % 10
    sum+=last_digit
    n = n//10

print(f"Sum is {sum}")
