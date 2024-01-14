import pygame
from modules.intro import show_intro_screen
from level_one import show_level_one
from level_two import show_level_two
from level_three import show_level_three

# Initialize game
pygame.init()

# Initialize pygame variables
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()


# Game Functions
show_intro_screen(screen, clock)
show_level_one(screen, clock)
#show_level_two(screen, clock)
show_level_three(screen, clock)
pygame.quit()