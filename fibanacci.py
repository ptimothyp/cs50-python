def fibanacci():
    result = []
    n1, n2 = 0, 1
    terms = int(input("How many terms? "))
    count = 0
    while count < terms:
        result.append(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
    return result

def main():
    print(fibanacci())

if __name__ == "__main__":
    main()
