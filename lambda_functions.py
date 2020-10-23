# Re-write the following piece of code using the lambda keyword:

# def func(x):
#    if x % 2 == 0:
#         return 'even'
#     else:
#         return 'odd'

# You are not supposed to handle input or invoke this function. Just re-write it!

x = int(input('Please enter a number: '))

func = (lambda x: 'even' if x % 2 == 0 else 'odd')  # noqa: E731

if __name__ == "__main__":
    print(func(x))
