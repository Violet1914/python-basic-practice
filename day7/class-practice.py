import winsound

class Clock:
    price = None
    id = None
    def ring(self):
        winsound.Beep(10000, 1000)

c = Clock()
c.ring()




