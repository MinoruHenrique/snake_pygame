import pygame

#Initialize game
pygame.init()

screen=pygame.display.set_mode((800,600), pygame.RESIZABLE)
pygame.display.set_caption("Snake game")

gameon=True

while gameon:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameon=False


pygame.quit()