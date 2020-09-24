def run():
    words = input()

    if ' ' in words:
        x = [word.capitalize() for word in words.split()]
        x[0] = x[0].lower()
        print(''.join(x))

    else:
        print(words.lower())


if __name__ == "__main__":
    run()
