# Check if input is prime or not
n = int(input("Enter the input "))

factors = []

for i in range(2, ((n//2)+1)):
    if n % i == 0:
        print(f"{n} is not a prime number")
        exit()

print(f"{n} is a prime number")
