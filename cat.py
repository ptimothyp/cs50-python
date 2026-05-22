def get_number():
    while True:
        i = int(input("What's n? "))
        if i > 0:
            break
    return i


def meow_for(i):
    print("For loop")
    for _ in range(i):
        print("meow")

    # print("meow\n" * i, end="")


def main():
    i = get_number()
    meow_for(i)


if __name__ == "__main__":
    main()
