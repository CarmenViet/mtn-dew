import pygame

def handle_movement(char_coordinates):
    keys_pressed=pygame.key.get_pressed()

    if keys_pressed[pygame.K_RIGHT]:
        char_coordinates["x"] += 7
    print (char_coordinates["x"])
    if keys_pressed[pygame.K_LEFT]:
        char_coordinates["x"] -= 7

    # Left boundary
    if char_coordinates["x"] < 0:
        char_coordinates["x"] = 0


def handle_jumping(char_physics):
    # Move character vertically based on jump velocity
    char_physics["coordinates"]["y"] += char_physics["jump_velocity"]

    # Gravity
    if char_physics["coordinates"]["y"] > 0:
        char_physics["jump_velocity"] -= 1
    
    # Stop going down when you hit the ground
    if char_physics["coordinates"]["y"] == 0:
        char_physics["jump_velocity"] = 0

    # Handle up button
    keys_pressed=pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP] and char_physics["coordinates"]["y"] == 0:
        char_physics["jump_velocity"] = 20
