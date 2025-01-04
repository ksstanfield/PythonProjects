#calculate BMI (Body Mass Index) divide weight in pounds by height in inches squared then multiplied by 703
#ask user for height in inches and weight in pounds
height = float(input("Enter your height in inches: "))
weight = float(input("Enter your weight in pounds: "))

#calculate BMI
bmi = int(weight) / (height**2) * 703
bmi_as_int = round(bmi)
if bmi_as_int < 18.5:
  print(f"Your BMI is {bmi_as_int}, you are underweight.")
elif bmi_as_int < 25:
  print(f"Your BMI is {bmi_as_int}, you have a normal weight.")
elif bmi_as_int < 30:
  print(f"Your BMI is {bmi_as_int}, you are slightly overweight.")
elif bmi_as_int < 35:
  print(f"Your BMI is {bmi_as_int}, you are obese.")
else:
  print(f"Your BMI is {bmi_as_int}, you are clinically obese.")