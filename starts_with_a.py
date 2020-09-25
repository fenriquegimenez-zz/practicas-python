# This program checks the input passed by the user and returns
# a list of those words if they starts whit 'a' or 'A'


def run():
    try:
        words_by_user = input(
            'Please enter a list of words separated by spaces: ')

        words = words_by_user.split()

        new_list = []

        for word in words:
            if word.startswith(('a', 'A')):
                new_list.append(word)

        print(new_list)
    except:
        if ' ' not in words:
            print('Please enter a list of words correctly')


if __name__ == "__main__":
    run()
