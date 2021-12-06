import math
n=int(input("Enter the number"))

for i in range(n):
    mid = math.ceil(n/2)
    length = int(i-1)
    print(' '*(mid-length), '*'*(length*2+1), ' '*(mid-length))
