# Let's say you have a dictionary matching your friends' names with their favorite flowers:

# favfl = {'Alex': 'field flowers', 'Kate': 'daffodil',
#          'Eva': 'artichoke flower', 'Daniel': 'tulip'}

# Your new friend Alice likes orchid the most: add this info to the favfl dict and print the dict.

# NB: Do not redefine the dictionary itself, just add the new element to the existing one.


def run():
    favfl = {'Alex': 'field flowers', 'Kate': 'daffodil',
             'Eva': 'artichoke flower', 'Daniel': 'tulip'}

    favfl['Alice'] = 'orchid'

    print(favfl['Alice'])


if __name__ == "__main__":
    run()
