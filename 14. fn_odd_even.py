# write a function to check whether a number is odd or even

def check_odd_or_even(number):
    return (number%2)==0

n = int(input("Enter the number: "))

if(check_odd_or_even(n)):
    print("The number is even")
else:
    print("The number is odd")
