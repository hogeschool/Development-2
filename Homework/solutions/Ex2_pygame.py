import pygame
from List import *
import time

# the same Car as part 1 of the exercise
class Car:
    def __init__(self, id):
        self.position = 0
        self.id = id
        self.verticalPosition = id # i will 'abuse' the id for this

    def move(self):
        self.position += 1
        print(self)
        return self

    def __str__(self):
        return "Car {} is at position: {}".format(self.id, self.position)


pygame.init()
size = width, height = 600, 600
white = 255, 255, 255
green = 50, 255, 100
screen = pygame.display.set_mode(size)

offset = 30
board_size = 10


def update(car):
    car.move()
    return car


def draw(car):
    # draw the car. Just an ugly green rectangle
    # pygame requires 4 parameters to define a rectangle: [x, y, width, height] of which we will only change the x
    position_and_size = [10*car.position, 32*car.verticalPosition, 30,30]
    pygame.draw.rect(screen, green, position_and_size)
    return car


def Main():
    # instantiate a car-object
    list = Node(Car(1),
                Node(Car(2),
                     Node(Car(3),
                          Node(Car(4),
                               Node(Car(5),
                                    Node(Car(6),
                                         Empty))))))

    # start the game-loop
    while True:
        pygame.event.pump()
        screen.fill(white)

        # Draw the cars
        list = list.Map(lambda car: draw(car))

        # update the cars
        list = list.Map(lambda car: update(car))

        time.sleep(0.1)
        pygame.display.flip()

Main()
