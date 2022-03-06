# write a function to generate all factors of a number

def generate_factors(number):
    # check if number is less than 0
    if number<=0:
        print("Invalid number")
        exit()

    print("Factors: ")

    # Check values up to n/2
    for i in range(1, ((number//2)+1)):
        if n % i == 0:
            print(i)

    print(number)



n = int(input("Enter the number: "))

generate_factors(n)
