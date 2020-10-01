
class Painting:

    title = input('Enter the painting title: ')
    painter = input('Enter the painting author: ')
    year = input('Enter the painting year of creation: ')

    def __init__(self, title, painter, year):
        self.title = title
        self.painter = painter
        self.year = year

print(f'"{Painting.title}" by {Painting.painter} ({Painting.year}) hangs in the Louvre.')