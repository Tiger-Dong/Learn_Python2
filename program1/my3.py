# BMI = kg/(m *m)
height = input("how tall are you (m)? ")
weight = input("what's your weight (kg)? ")
print("your height is " + str(height) + "m")
print("your weight is " + str(weight) + "kg")

BMI_1 = weight / (height * height)
BMI = round( BMI_1,2)
print("your BMI is ") and (BMI) 


BMI_1 = weight / (height * height)
print("Your BMI is " + str(round(BMI_1,2)))