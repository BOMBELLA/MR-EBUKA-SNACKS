#collect an input of weight and height
#using the formular in the statement
#use a control statement 

weight = int(input("Enter your weight : "))
height = int(input("Enter your height : "))
bmi = weight / (height * height)
if weight < 18.5:
       print("Underweight")

elif weight <== 18.5 and <== 24.9:
       print("Normal")

elif weight <== 25 and <== 29.9:
       print("Overweight")

elif weight >= 30:
       print("Obese")

