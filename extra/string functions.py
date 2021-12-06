first_name = input("Enter the first name: ")
last_name = input("Enter the last name: ")

full_name = f"{first_name} {last_name}"
print(f"Full name is {full_name}")

n = int(input("Enter the number:"))

if n not in range(10):
    print("number should be between 1-10")
    exit()

for i in range(n):
    print('*'*(i+1))

print(f"until {n}th letter in name {full_name[:n]}")


