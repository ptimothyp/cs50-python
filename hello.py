def hello(to="world"):
    return f"hello, {to}"


def main():
    hello()
    name = input("What's your name? ")
    print(hello(name))


if __name__ == "__main__":
    main()
