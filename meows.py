class Cat:
    # Const not enfoced convenstion is all CAPS
    MEOWS = 3

    def meow(self) -> None:
        for _ in range(Cat.MEOWS):
            print("meow", end=" ")


def main():
    cat = Cat()
    meows:str = cat.meow()
    print(meows)


if __name__ == "__main__":
    main()
