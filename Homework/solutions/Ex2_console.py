from List import *

class Car:
    def __init__(self, id):
        self.position = 0
        self.id = id

    def move(self):
        self.position += 1
        print(self)
        return self

    def __str__(self):
        return "Car {} is at position: {}".format(self.id, self.position)


list = Node(Car(1),
        Node(Car(2),
        Node(Car(3),
        Node(Car(4),
        Node(Car(5),
        Node(Car(6),
        Empty))))))

for i in range(0, 10):
    list = list.Map(lambda car: car.move())

