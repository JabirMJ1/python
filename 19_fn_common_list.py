# takes 2 list and returns true if they have atleast 1 common element

def input_list(length):
    print("Enter the list")
    temp_list = []
    for i in range(length):
        temp_list.append(input())
    return temp_list

def check_common(list_1, list_2):
    for i in list_1:
        for j in list_2:
            if(i==j):
                return(True)


len1=int(input("Enter the length of list 1: "))
list1 = input_list(len1)

len2=int(input("Enter the length of list 2: "))
list2 = input_list(len2)


if(check_common(list1, list2)):
    print("Common elements exists")
else:
    print("No Common elements")
