# prime number within a range
start = int(input("Enter the start value: "))
end = int(input("Enter the end value: "))

f=0
for i in range(start, end+1):
    f=0
    for j in range(2, ((i//2)+1)):
        if i % j == 0:
            f = f + 1
            break
    if f==0 and i!=1:
        print(i)
