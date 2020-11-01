import pygame, random
from pygame.locals import *
import sys
from platform import Platforms

pygame.init()

screen_info = pygame.display.Info()

#setting the screen width and height
size = (width, height) = (screen_info.current_w, screen_info.current_h)
clock = pygame.time.Clock()
color = (88, 59, 116)

player_list = pygame.sprite.Group()
platforms = pygame.sprite.Group()

def init():
  for i in range(height//100):
    for j in range(width//420):
      plat = Platforms((random.randint()))

def main():
  global player
  game_over = False
  
  while True:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()

if __name__ == "__main__":
  main()