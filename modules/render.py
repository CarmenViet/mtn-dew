from modules.images import *

def render_protag(screen, char_coordinates, ground_level):
    screen.blit(shoellieila_image, (300, ground_level - char_coordinates["y"]))

def render_stage(screen, char_coordinates, stage_background_image):
    screen.fill("black")
    screen.blit(stage_background_image, (-char_coordinates["x"], 0))

def render_neighbor(screen, char_coordinates, neighbor_image, neighbor_base_coordinates):
    screen.blit(neighbor_image, (-char_coordinates["x"] + neighbor_base_coordinates[0], neighbor_base_coordinates[1]))