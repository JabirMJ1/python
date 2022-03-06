# Write a function to find the sum of the digits of a number

def sum_of_digits(number):
    sum = 0
    while number > 0:
        last_digit = number % 10
        sum += last_digit
        number = number // 10

    return sum


n = int(input("Enter the number: "))

print(sum_of_digits(n))
        
