# create your dictionary here
def run():
    from collections.abc import Hashable

    objects_dict = {}
    dictio = {}
    lista = []
    tupla = ('hola',)

    objects = ['hola', 2, 2.6, dictio, lista, tupla]

    for i in objects:
        if isinstance(i, Hashable):
            objects_dict[i] = hash(i)

    print(objects_dict)

    return None


if __name__ == "__main__":
    run()
