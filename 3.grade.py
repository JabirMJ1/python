mark1 = int(input("Enter the mark of the First subject 1: "))
mark2 = int(input("Enter the mark of the First subject 2: "))
mark3 = int(input("Enter the mark of the First subject 3: "))
mark4 = int(input("Enter the mark of the First subject 4: "))
mark5 = int(input("Enter the mark of the First subject 5: "))


total = mark1 + mark2 + mark3 + mark4 + mark5

average = total / 5

print(f"\nTotal mark is {total}\n")
print(f"Average mark is {average}\n")

if average>=80:
    print("A grade")
elif average>=70:
    print("B grade")
elif average>=60:
    print("C grade")
elif average>=50:
    print("D grade")
elif average>=40:
    print("E grade")
else:
    print("Failed")
    
