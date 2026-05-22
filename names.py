names = []


def write_input_lines():
    for _ in range(3):
        name = input("What's your name? ")
        names.append(name)
        with open("./names.txt", "a") as file:
            for name in sorted(names):
                file.write(name + "\n")


with open("./names.txt") as file:
    lines = file.readlines()
    # lines = sorted(lines, reverse=True)
    lines = sorted(lines)
    for line in lines:
        print("hello,", line.rstrip())
