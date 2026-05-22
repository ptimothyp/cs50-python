def print_column(height):
    for _ in range(height):
        print("#")


def print_row(width):
    for _ in range(width):
        print("[?]", end=" ")


def print_square(height, width):
    print()
    for _ in range(height):
        print("#" * width)


def main():
    print_column(3)
    print_row(3)
    print_square(3, 5)


if __name__ == "__main__":
    main()
