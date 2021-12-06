# write print fibonocci series
n = int(input("Enter the count of fibonocci: "))
first = 0
second = 1

# count is 0
if n < 0:
    print("Count is 0")
    exit()

# print first if n greater than 1
if n>=1:
    print(first)

# print all if greater than 1
if n >= 2:
    print(second)
    for i in range(1, n-1):
        print(first + second)
        temp = first
        first = second
        second = temp + second
        
        
