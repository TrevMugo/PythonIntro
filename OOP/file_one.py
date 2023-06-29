class Fruit:
    def __init__(self, name, colour, size, price):
        self.name = name
        self.colour = colour
        self.size = size
        self.price = price


class Car:
    def __init__(self, name, model, colour, reg_no, price):
        self.name = name
        self.model = model
        self.colour = colour
        self.reg_no = reg_no
        self.price = price


x1 = Car("Mazda", "CX5", "Wine_red", "KCW_3645R", "3.5M")
print(x1.model)


class Employee:
    def __init__(self, name, dept, salary):
        self.name = name
        self.dept = dept
        self.salary = salary

    def login(self):
        print("Hello, I can login")

    def register(self):
        print("Hello, I can register")


employeeOne = Employee("Joseph", "Accounts", "30,0000")
employeeOne.register()
