# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "requests>=2.32.5",
#     "cowsay>=6.1",
# ]
# ///

from square import square


def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


def main():
    test_positive()
    test_negative()
    test_zero()


if __name__ == "__main__":
    main()
