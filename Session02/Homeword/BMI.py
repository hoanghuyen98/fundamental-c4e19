height = int(input("Enter the height : "))
weight = int(input("Enter the weight : "))
BMI = weight/((height*height)*(10**(-4)))
print("BMI = ", BMI)
if BMI < 16:
    print("==> Severely underweight !!")
elif BMI < 18.5:
    print("==> Underweight !!")
elif BMI < 25:
    print("==> Normal !!")
elif BMI < 30:
    print("==> Overweight !!")
else :
    print("==> Obese !!")
