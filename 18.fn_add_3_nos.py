# Write a function to calculate the sum of 3 numbers.
# - If all the given numbers are equal return thrice their sum

def sum_of_three_numbers(n1, n2, n3):
    if n1==n2==n3:
        return (n1+n2+n3)*3
    else:
        return (n1+n2+n3)

num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2: "))
num3 = int(input("Enter the number 3: "))

print(sum_of_three_numbers(num1, num2, num3))
