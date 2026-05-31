class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house


    @classmethod
    def get(cls):
        name = input("What's your name? ")
        house =  input("What's your house? ")
        try:
            return cls(name,house)
        except ValueError:
            None




    @property
    def house(self):
        return self._house

    @house.setter
    def house(self,house):
        if house not in ["Gryffindor","Hufflepuff","Ravenclaw","Slythrerin"]:
            raise ValueError("Invalid house")
        self._house = house

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Empty name")
        self._name = name

    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = Student.get()
    if not student:
        print("Empty student")
    else:
        print(student)


if __name__ == "__main__":
    main()
