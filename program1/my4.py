#BMI = weight/(height*height)
height = input("How tall are you?(m)")
weight = input("what is your weight?(kg)")
BMI = round(float(weight) / (height* height),2)
# 
print("Your height is " + str(height))
print("Your weight is " + str(weight))
print("Your BMI is " + str(BMI))
if(BMI > 29.9):
  print("Obesity")
elif(BMI > 24.9) and (BMI <30):
  print("Over weight")
elif(BMI > 18.4) and (BMI <25):
  print("Normal weigh")
elif(BMI < 18.6):
  print("Underweight")
  
