import math


def motto():
    print("Sample Motto")


motto()


def vision():
    print("This is our vision")


vision()


def add():
    x = 10
    y = 20
    z = x + y
    print(z)


add()
add()


def avg(x, y, z):
    average = (x + y + z) / 3
    print("Your average is" + str(average))


avg(98, 68, 35)
avg(98, 30, 58)
avg(76, 17, 48)


def bmiCalc(w, h):
    bmi = w / pow(h, 2)
    if bmi <= 18:
        print("UnderWeight")
    elif bmi <= 29:
        print("NormalWeight")
    elif bmi <= 34:
        print("OverWeight")
    else:
        print("Obese")


bmiCalc(90, 1.7)
bmiCalc(40, .7)
bmiCalc(190, 1.7)


# A Simple Grading System
def grades(mith, eng, kis):
    avrg = (mith + eng + kis) / 3
    if avrg >= 80:
        print("You got an A")
    elif avrg >= 70:
        print("You got a B")
    elif avrg >= 60:
        print("You got a C")
    elif avrg >= 50:
        print("You got a D")
    else:
        print("You got an E")


grades(70, 76, 75)
grades(88, 79, 87)
grades(78, 89, 52)
grades(42, 88, 65)
grades(78, 68, 59)


def login(email, password):
    if email == "user@example.com" and password == "user123":
        grades(90, 88, 97)
    else:
        print("Login Failed")


login("user@example.com", "user123")


def areaCircle(r):
    area = math.pi * pow(r, 2)
    return area


print(areaCircle(7))

