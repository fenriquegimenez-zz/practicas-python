# Read a string with digits from the input and convert each number to an integer. 
# Include only odd digits in your list and print what you'll get.

def run():
    sample = input('Please enter a sequence of digits: ')
    odd_list = []

    for x in sample:
        if int(x) % 2 != 0:
            odd_list.append(int(x))
    print(odd_list)
    return None    

if __name__ == "__main__":
    run()