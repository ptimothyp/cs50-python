def AddInt():
    x = int(input("What's x?"))
    y = int(input("What's y?"))

    print(x + y)


def AddFloat():
    x1 = float(input("What's x?"))
    y1 = float(input("What's y?"))

    z = round(x1 + y1)

    # formats , every 3 digits
    print(f"{z:,}")


def DivideFloat():
    x = float(input("What's x?"))
    y = float(input("What's y?"))

    z = x / y

    # formats , to 2 digits after decimal point
    print(f"{z:.2f}")


def square(n):
    return n * n


def main():
    x = int(input("What's x?"))
    print("x squared is", square(x))


if __name__ == "__main__":
    main()
