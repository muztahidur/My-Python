print("Find your BMI")
Weight = float(input("Inter your weight (KG): "))
height = float(input("inter your height (ft): "))

height_in_m = float(height * 0.3048)

BMI = Weight / (height_in_m ** 2)
print ("your BMI is", (BMI))

if BMI < 18.5:
    print("You are Underweight")
    
elif BMI < 25:
    print("Your Weight is perfect")

elif BMI <30:
    print("You are overweight")
    
else:
    print("You are obese")