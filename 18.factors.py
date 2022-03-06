# factors of an inputted number

n = int(input("Enter the number: "))

# Check if n is greater than 0
if n <= 0:
    print("Cant provide factors: ")
    exit()

print("factors:")

# Check value up to n/2
for i in range(1, ((n//2)+1)):
    if n % i == 0:
        print(i)

print(n)
