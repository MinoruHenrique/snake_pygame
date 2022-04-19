import pygame
#PARAMS
BG_COLOR=(0,0,100)
RESOURCE_FOLDER="resources/"

def run():
    pygame.init()

    screen =initialize_screen()

    gameon=True

    while gameon:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameon=False


    pygame.quit()

def initialize_screen(BG_COLOR=BG_COLOR):
    screen=pygame.display.set_mode((800,600), pygame.RESIZABLE)
    pygame.display.set_caption("Snake game")
    screen.fill(BG_COLOR)
    pygame.display.set_icon(pygame.image.load(RESOURCE_FOLDER+"icon.png"))

    pygame.display.flip()
    
    return screen