class Student:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def register(self):
        print("I can register using" + self.email)

    def login(self):
        print("I can login using" + self.email)


class Lecturer(Student):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)

    def submit_results(self):
        print("I can submit results")


class Hod(Lecturer):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)

    def standardize_results(self):
        print("I can standardize results")

