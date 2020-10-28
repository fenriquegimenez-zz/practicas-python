from collections.abc import Hashable


def run():
    object_list = [1, 397, 27468, -95, 1309, 397, -539874, -240767, -95, 397]

    hashes = []
    counter = 0

    for i in object_list:
        if isinstance(i, Hashable):
            hashes.append(hash(i))
            print(hashes, counter)
        if i in hashes:
            counter += 1

    if len(hashes) == 0:
        print(0)
    else:
        print(counter)


if __name__ == "__main__":
    run()
