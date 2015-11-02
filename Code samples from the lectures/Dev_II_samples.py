########################
# lecture one - problem
########################
playerOneName = "P1"
playerOnePositionX = 0.0
playerOnePositionY = 0.0

playerTwoName = "P2"
playerTwoPositionX = 5.0
playerTwoPositionY = 0.0

playerThreeName = "P3"
playerThreePositionX = 10.0
playerThreePositionY = 0.0

########################
# lecture two - solution
########################
class Player:
  def __init__(self, name, posX, posY):
    self.Name = name
    self.PositionX = posX
    self.PositionY = posY

playerOne   = Player("P1", 0.0, 0.0)
playerTwo   = Player("P2", 5.0, 0.0)
playerThree = Player("P3", 10.0, 0.0)

print(playerOne.Name + " is at " + str(playerOne.PositionX) + "," + str(playerOne.PositionY))
print(playerTwo.Name + " is at " + str(playerTwo.PositionX) + "," + str(playerTwo.PositionY))
print(playerThree.Name + " is at " + str(playerThree.PositionX) + "," + str(playerThree.PositionY))

########################
# lecture three - refined
########################
class Vector2:
  def __init__(self, x, y):
    self.X = x
    self.Y = y

class PlayerRefined:
  def __init__(self, name, posX, posY):
    self.Name = name
    self.Position = Vector2(posX,posY)

playerOne   = PlayerRefined("P1", 0.0, 0.0)
playerTwo   = PlayerRefined("P2", 5.0, 0.0)
playerThree = PlayerRefined("P3", 10.0, 0.0)

print(playerOne.Name + " is at " + str(playerOne.Position.X) + "," + str(playerOne.Position.Y))
print(playerTwo.Name + " is at " + str(playerTwo.Position.X) + "," + str(playerTwo.Position.Y))
print(playerThree.Name + " is at " + str(playerThree.Position.X) + "," + str(playerThree.Position.Y))
