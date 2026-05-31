def main():
    yell("hello", "world", "yoyoyo")

def yell(*phrases):
    # upperPhrases = map(str.upper, phrases)
    upperPhrases = [phrase.upper() for phrase in phrases]
    print(*upperPhrases)


if __name__ == "__main__":
    main()
