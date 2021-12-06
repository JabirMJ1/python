# reverse of a number
n = int(input("Enter the number: "))

reverse = 0

while n>0:
    last_digit = n % 10
    reverse = (reverse * 10) + last_digit
    n = n // 10

print(f"reverse is {reverse}")
