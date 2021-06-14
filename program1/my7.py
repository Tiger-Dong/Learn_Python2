people = []
name = input("What is your name?")

while name != "bye" :
	
	print("Hi " + name)
	name = input("What is your name?")
	people.append(name)
	
print("I've said Hi to " + str(len(people)) + " people.")