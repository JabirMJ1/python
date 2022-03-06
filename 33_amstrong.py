# function to check if the number is amstrong or not 153, 370, 371

def check_amstrong(number):
    temp=number
    sum=0
    while(temp>0):
        last = temp % 10
        sum = sum + (last**3)
        temp = temp // 10
    if(sum==number):
        return(True)
    else:
        return(False)

n = int(input("Enter the number: "))

if(check_amstrong(n)):
    print(f"{n} is an amstrong number")
else:
    print(f"{n} is not an amstrong number")
        
