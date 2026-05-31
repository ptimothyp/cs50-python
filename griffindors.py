students = [
        {"name": "Hermoine", "house": "Gryffindor" },
        {"name": "Harry", "house": "Gryffindor" },
        {"name": "Ron", "house": "Gryffindor" },
        {"name": "Draco", "house": "Slytherlin" }
        ]

# print(students)
print(*sorted([student["name"] for student in students if student["house"] == "Gryffindor"]), sep=", ")

def is_griffindor(s):
    return s["house"] == "Gryffindor"

print(*sorted(filter(lambda s: s["house"] == "Gryffindor", students), key=lambda s: s["name"]))


students = ['harry',"hermoine","ron"]
griffindors = {student : "Griffindor" for student in students}
print(griffindors)


for i,student in enumerate(students):
    print(i+1, student)
