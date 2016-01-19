from List import *
from random import randint


class Node2D:
    def __init__(self, Head):
        self.Head = Head
        self.TailLeft = None
        self.TailRight = None
        self.TailUp = None
        self.TailDown = None
        self.Final = False


class Crossing:
    def __init__(self, Position, Name):
        self.Position = Position
        self.Name = Name

    def __str__(self):
        return self.Name


class Position:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def __str__(self):
        return "position: ({}, {})".format(self.X, self.Y)


class Car:
    def __init__(self, id, position):
        self.position = position
        self.id = id

    def move(self):
        """Moves the car to a neighbouring crossing"""
        possible_directions = Empty

        # Check all possible directions
        if self.position.TailRight is not None:
            possible_directions = Node(self.position.TailRight, possible_directions)
        if self.position.TailLeft is not None:
            possible_directions = Node(self.position.TailLeft, possible_directions)
        if self.position.TailUp is not None:
            possible_directions = Node(self.position.TailUp, possible_directions)
        if self.position.TailDown is not None:
            possible_directions = Node(self.position.TailDown, possible_directions)

        # pick a random number
        length = possible_directions.Length()
        random_index = randint(0, length-1)

        # get a random direction. Note we extended our List with a get function
        self.position = possible_directions.Get(random_index, 0)

        return self

    def __str__(self):
        return "Car {} is at {}".format(self.id, self.position.Head.Name)


# make some nodes with crossings as head. Note we do not set the tails just yet
cs = Node2D(Crossing(Position(10, 10), "RotterdamCS"))
hp = Node2D(Crossing(Position(400, 10), "Hofplein"))
ep = Node2D(Crossing(Position(10, 400), "Eendrachtsplein"))
br = Node2D(Crossing(Position(400, 400), "Beurs"))
bl = Node2D(Crossing(Position(500, 400), "Blaak"))


# now we set the tails
cs.TailRight = hp
cs.TailDown = ep
hp.TailLeft = cs
hp.TailDown = br
ep.TailUp = cs
ep.TailRight = br
br.TailUp = hp
br.TailLeft = ep
br.TailRight = bl
bl.TailLeft = br

# Cruise around in our car
c = Car(1, bl)
for i in range(20):
    c.move()
    print(c)
