# Using single function perform all arithemetic fuctions

def arithemetic(n1, n2):
    return(n1+n2, n1-n2, n1/n2, n1*n2)

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

ar_list = arithemetic(number1, number2)
print(f"sum = {ar_list[0]}")
print(f"diff = {ar_list[1]}")
print(f"div = {ar_list[2]}")
print(f"mul = {ar_list[3]}")
