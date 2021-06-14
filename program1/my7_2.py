number = [3,1,4,1,5,9,2,6]
sum = 0
count = 0
while count < len(number):
	sum = sum + number[count]
	count = count + 1

average = float(sum)/ len(number)

print("the numbers are {}".format(number))
print("the average of these numbers is {}".format(average))