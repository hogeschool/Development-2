import pygame


# the same Car as part 1 of the exercise
class Car:
    def __init__(self):
        self.position = 0

    def move(self):
        self.position += 1
        print(self.position)

    def __str__(self):
        return "the car is at position: ".format(self.position)


def Main():
    pygame.init()
    size = width, height = 600, 600
    white = 255, 255, 255
    green = 50, 255, 100
    screen = pygame.display.set_mode(size)

    offset = 30
    board_size = 10

    #instantiate a car-object
    c = Car()

    #start the game-loop
    while True:
        pygame.event.pump()
        screen.fill(white)


        # draw the car. Just an ugly green rectangle
        # pygame requires 4 parameters to define a rectangle: [x, y, width, height] of which we will only change the x
        position_and_size = [10*c.position, 30, 30,30]
        pygame.draw.rect(screen, green, position_and_size)

        # update the car
        c.move()

        pygame.display.flip()

Main()
