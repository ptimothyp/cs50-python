import csv

students = []
with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(
            {"name": row["name"], "house": row["house"], "home": row["home"]}
        )


def get_name(student):
    return student["name"]


def print_student(student):
    print(f"{student['name']} is in {student['house']}")


def print_heading(heading):
    print(heading)
    print("*" * len(heading))


def read_from_file():
    print_heading("\nSorted by name")
    for student in sorted(students, key=get_name):
        print_student(student)

    print_heading("\nSorted by house")
    for student in sorted(students, key=lambda student: student["house"]):
        print_student(student)


def write_to_file():
    name = input("What's your name? ")
    home = input("Where is your home? ")
    with open("students_w.csv", "a") as file:
        # fieldnames -> order of the headings in the csv file
        writer = csv.DictWriter(file, fieldnames=["home", "name"])
        writer.writerow({"home": home, "name": name})


def main():
    # read_from_file()
    write_to_file()


if __name__ == "__main__":
    main()
