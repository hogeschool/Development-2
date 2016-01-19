import pygame
from List import *
import time


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
cb = Node(Station(Position(200, 500), "Capelse brug"),kz)
gw = Node(Station(Position(400, 80), "Gerdesiaweg"),cb)

# stations = Node(kz, Node(cb, Node(gw, Empty)))

metro = Metro(gw)


pygame.init()
size = width, height = 600, 600
white = 255, 255, 255
green = 50, 255, 100
black = 0, 0, 0
screen = pygame.display.set_mode(size)

offset = 30
board_size = 10


def update(metro):
    metro.Move()
    return metro


def draw(metro):
    position_and_size = [metro.CurrentStation.head.position.X,
                         metro.CurrentStation.head.position.Y,
                         30, 30]
    pygame.draw.rect(screen, green, position_and_size)
    return metro


def draw_stations(stations):
    points = []
    stations.Map(lambda station: points.append((station.position.X, station.position.Y)))
    pygame.draw.lines(screen, black, False, points)


def Main():
    # instantiate a car-object
    # list = Node(Car(1),
    #             Node(Car(2),
    #                  Node(Car(3),
    #                       Node(Car(4),
    #                            Node(Car(5),
    #                                 Node(Car(6),
    #                                      Empty))))))

    # start the game-loop
    while True:
        pygame.event.pump()
        screen.fill(white)
        draw_stations(gw)

        # Draw the cars
        # list = list.Map(lambda car: draw(car))
        draw(metro)

        # update the cars
        # list = list.Map(lambda car: update(car))
        update(metro)

        time.sleep(1)
        pygame.display.flip()

Main()
