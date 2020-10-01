import pygame
x = pygame.init()
gameWindow = pygame.display.set_mode((600,300))
pygame.display.set_caption("Snake Game")
exit_game = False
game_over = False
while not exit_game:
   for event in pygame.event.get():
      print(event)
pygame.quit()
quit()