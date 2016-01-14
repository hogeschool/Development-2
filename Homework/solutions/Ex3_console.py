from List import *

class Metro:
    def __init__(self, currentStation):
        self.CurrentStation = currentStation

    def Move(self):
        if not self.CurrentStation.tail.IsEmpty():
            self.CurrentStation = self.CurrentStation.tail
        else:
            print("I've reached my end destination")

    def __str__(self):
        return "Metro is at {}".format(self.CurrentStation.head)


class Station:
    def __init__(self, position, name):
        self.position = position
        self.name = name

    def __str__(self):
        return "Station - {} at - {}".format(self.name, self.position)


class Position:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def __str__(self):
        return "position: ({}, {})".format(self.X, self.Y)

kz = Node(Station(Position(10, 30), "Kralingse zoom"), Empty)
cb = Node(Station(Position(20, 50), "Capelse brug"),kz)
gw = Node(Station(Position(40, 80), "Gerdesiaweg"),cb)

stations = Node(kz, Node(cb, Node(gw, Empty)))

metro = Metro(gw)

print("Start")
print(metro)
metro.Move()
print(metro)
metro.Move()
print(metro)
metro.Move()
print(metro)
metro.Move()
print(metro)

