class Wizard:
    def __init__(self,name):
        if not name:
            raise ValueError
        self.name = name

class Student(Wizard):
    def __init__(self,name,house):
        super().__init__(name)
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} is in {self.house}"


    ...
class Professor(Wizard):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject

    def __str__(self):
        return f"{self.name} teaches {self.subject}"
    ...


def main():
    student = Student("Harry", "Griffindor")
    print(student)
    professor = Professor("Dumbeldoor", "Wizardry")
    print(professor)


if __name__ == "__main__":
    main()
