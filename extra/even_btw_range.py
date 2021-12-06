# print even numbers between two inputted numbers

start = int(input("Enter the start limit: "))
last = int(input("Enter the end limit: "))

# set start as even number
if start % 2!=0:
    start+=1
    
# check if start greater than last
if start >= last:
    if start > last:
        print("Start is greater than or equal to last")
    else:
        print(start)
    exit()

# print all numbers
for i in range(start, last+1, 2):
    print(i)


