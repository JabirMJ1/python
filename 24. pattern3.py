# pattern triangle

i = 1
max = 5
flag = False

while i > 0:
    print('* '*i)
    if i == max:
        flag = True

    if flag:
        i-=1
    else:
        i+=1
