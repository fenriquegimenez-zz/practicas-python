from collections.abc import Hashable


def run():
    some_object = dict()

    return "hashable" if isinstance(some_object, Hashable) else "Not hashable"


if __name__ == "__main__":
    print(run())
