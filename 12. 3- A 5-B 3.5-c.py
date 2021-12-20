list = [3,5,15,20,18,7,32,1]

for i in list:
    if (i % 3 == 0) and (i % 5 ==0 ):
        print(f"{i} : C")
    elif i % 3 == 0:
        print(f"{i} : A")
    elif i % 5 == 0:
        print(f"{i} : B")
