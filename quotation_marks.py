# This program checks if the input passed by the user has double quotation marks and }
# print it without them.

def run():
    string = input('Please enter a phrase: ')
    def printer(string):
        if string.startswith('"') and string.endswith('"'):
            return string[1:-1:]
        else:
            return string
    print(printer(string))
    return None

if __name__ == "__main__":
    run()