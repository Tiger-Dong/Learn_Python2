number = [0,3,0,0,0,3,0,4]
sum = 0
round = 0
while round < len(number):
	sum = sum + number[round]
	round = round +1
average = sum/len(number)
print("There are {} nambers".format(len(number)))
print("The average is {}".format(average))