class Car:
    def __init__(self):
        self.position = 0

    def move(self):
        self.position += 1
        print(self.position)

    def __str__(self):
        return "the car is at position: ".format(self.position)

c = Car()
c.move()
c.move()
c.move()
