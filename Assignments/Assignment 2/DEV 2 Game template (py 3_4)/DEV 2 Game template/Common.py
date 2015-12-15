import os, pygame


#USE THIS FUNCTION (IF NECESSARY) TO ROTATE A TEXTURE. NOTE. THIS FUNCTION IS IMMUTABLE. IT RETURNS ALWAYS A NEW TEXTURE
def set_orientation(prev_p, new_p, texture):
  if prev_p != None and new_p != None:
    img = texture
    if prev_p.Position.X > new_p.Position.X:
      img = pygame.transform.flip(img, -1, 0)
    if prev_p.Position.Y < new_p.Position.Y:
      img = pygame.transform.rotate(img, 270)
    if prev_p.Position.Y > new_p.Position.Y:
      img = pygame.transform.rotate(img, -270)
    return img
  else: return texture