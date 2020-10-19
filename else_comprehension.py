# Write a program that converts a given list into a list with binary values: either 1 or 0.
# If the number in the initial list was greater than 0, in the binary list there should be 1,
# and if the number was less or equal, in the new list you should write 0. Naturally,
# use the list comprehension and print the result.

Given list: a list with integer numbers, e.g. [5, 0, 4, -10].

Output list: a list consisting of ones and zeros, e.g. [1, 0, 1, 0].


def run():
    old_list = [int(num) for num in input().split()]

    binary_list = [1 if i > 0 else 0 for i in old_list]

    print(binary_list)


if __name__ == "__main__":
    run()
