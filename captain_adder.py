# Define a function that will add the word "captain" before the name of a person.

# The function should be named captain_adder, take one argument name and print the string,
# i.e. it doesn't have to return anything.

# You don't need to call your function, only implement it. Also, you don't need to take input,
# the name variable should come to your function as an argument.

name = input('Please enter your name: ')


def captain_adder(name):
    return f'captain {name}'


if __name__ == "__main__":
    print(captain_adder(name))
