print("Enter your Weight(KG) and Height(CM) to Check your BMI")
weight = float(input("Weight (KG): "))
height = float(input("Height (CM): "))

height_in_cm = height / 100
bmi = weight / (height_in_cm ** 2)

if bmi >= 25:
    print("Overweight")

elif bmi >= 18.5:
    print("Normal Weight")

else:
    print("Underweight")
