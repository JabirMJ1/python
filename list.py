list1 = [5,4,3,2,1]
list2 = [5,6,7,8,9]
sum1=sum2=0
common=[]


# Check if the lengths are same
if len(list1) != len(list2):
	print("Length: not same")
else:
	print("Length: Same")

# loop to get sum
for i in list1:
	sum1 = sum1 + i
		
for j in list2:
	sum2 = sum2 + j

# Check indivitual sum
# print("Sum of list1 ", sum1)
# print("Sum of list2 ", sum2)
if sum1 != sum2:
	print("Sum: Not same")
else:
	print("Sum: Same")


# get any common elements
for i in list1:
	for j in list2:
		if i == j:
			common.append(i)

if common == []:
	print("No Common Elements")
else:
	print("Common Elements")

print(common)
