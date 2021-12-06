# palindrome of a number
n = int(input("Enter the number: "))

backup = n
reverse = 0

while n>0:
    last_digit = n % 10
    reverse = (reverse * 10) + last_digit
    n = n / 10

if reverse==backup:
    print(f"{backup} is a palindrome")
else:
    print(f"{backup} is not a palindrome")
