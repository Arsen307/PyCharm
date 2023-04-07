class iteracja:
    def __init__(self, chyslo):
        self.chyslo = chyslo
    def __iter__(self):
        for predmet in self.chyslo:
            yield predmet

generator = iteracja([5,7,2,9,4,3,10])
for predmet in generator:
    print(predmet)