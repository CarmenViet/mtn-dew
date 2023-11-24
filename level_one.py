import pygame
from modules.render import *
from modules.movement import *
from modules.images import *


def show_level_one(screen, clock):
    char_physics = {
        "coordinates": {
            "x": 0,
            "y": 0
        },
        "jump_velocity": 0
    }

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        handle_movement(char_physics["coordinates"])
        handle_jumping(char_physics)

        render_stage(screen, char_physics["coordinates"], neighbor1_image)
        render_protag(screen, char_physics["coordinates"], ground_level=400)
        render_neighbor(screen, char_physics["coordinates"], jollibee_image, neighbor_base_coordinates=[3156, 400])

        pygame.display.update()
        clock.tick(60)