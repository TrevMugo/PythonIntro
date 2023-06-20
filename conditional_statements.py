age = 3
if age < 18:
    print("TRUE")
else:
    print("FALSE")

x = 10
y = 20
if x < y and y > 30:
    print("TRUE")
else:
    print("FALSE")

if x < y or y > 50:
    print("TRUE")
else:
    print("FALSE")

marks = 10
if marks < 40:
    print("E")
elif marks < 50:
    print("D")
elif marks < 60:
    print("C")
elif marks < 70:
    print("B")
else:
    print("A")

betNo = 0
if betNo == 1:
    print("Yow won a dog!!")
elif betNo == 2:
    print("You won a cat!!")
elif betNo == 3:
    print("You won a horse!!")
elif betNo == 4:
    print("You won a chick!!")
else:
    print("Please input any number from 1 to 4 to win an animal!")


interest = 10
print("If your interest is"+str(interest)+",then,")
if interest > 6:
    print("your loan is a bad loan")
elif interest > 3:
    print("your loan is a good loan")
else:
    print("your loan is a scam")

weight = 65
h = 1.5

BMI = weight / (h * h)

if BMI < 18:
    print("Your BMI is " + str(BMI) + ",making you Underweight")

elif BMI < 29:
    print("Your BMI is " + str(BMI) + ",making you Normal-weight")

elif BMI < 34:
    print("Your BMI is " + str(BMI) + ",making you Overweight")

else:
    print("Your BMI is " + str(BMI) + ",making you Obese")
