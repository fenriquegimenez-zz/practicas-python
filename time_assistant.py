# You are trying to write a personal assistant, and one of its tasks is to print the local time for a user.
# Write a piece of code that would do that using the strftime() function with the output format: "It's 09:11.".
from time import strftime, localtime

if __name__ == "__main__":
    print(f"It\'s {strftime('%H:%M', localtime())}")
