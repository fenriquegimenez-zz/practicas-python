string = 'turtle'


def concat(strng, sep=':'):
    if ' ' not in strng:
        return strng
    elif type(strng) == 'tuple':
        return ' '.join(strng)


concat(string, sep)
