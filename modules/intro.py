import pygame
from modules.images import *

def show_intro_screen(screen, clock):
    screen.blit(intro_image,(0,0))
    pygame.display.update()
    user_has_clicked = False

    while user_has_clicked == False:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                user_has_clicked = True
            if event.type == pygame.QUIT:
                pygame.quit()

        clock.tick(60)