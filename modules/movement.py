import pygame

def handle_movement(char_coordinates):
    keys_pressed=pygame.key.get_pressed()

    if keys_pressed[pygame.K_RIGHT]:
        char_coordinates["x"] += 7
    #print (char_coordinates["x"])
    if keys_pressed[pygame.K_LEFT]:
        char_coordinates["x"] -= 7

    # Left boundary
    if char_coordinates["x"] < 0:
        char_coordinates["x"] = 0


def handle_jumping(char_physics, platform_list, ground_level):
    # Move character vertically based on jump velocity
    char_physics["coordinates"]["y"] += char_physics["jump_velocity"]

    # Gravity
    if char_physics["coordinates"]["y"] > 0:
        char_physics["jump_velocity"] -= 1
    
    check_distance = -char_physics["jump_velocity"]
    platform_distance = check_for_object(char_physics, platform_list, check_distance, ground_level)

    # Stop going down when you hit the ground
    if char_physics["coordinates"]["y"] == 0:
        char_physics["jump_velocity"] = 0
    elif platform_distance["down"] != None: #and char_physics["jump_velocity"] < 0
        check_for_object(char_physics, platform_list, check_distance, ground_level)
        char_physics["jump_velocity"] = 0
        char_physics["coordinates"]["y"] -= platform_distance["down"] 


def handle_jump_press(char_physics):
    # Handle up button
    keys_pressed=pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP] and char_physics["coordinates"]["y"] == 0:
        char_physics["jump_velocity"] = 20

def check_for_object(char_physics, object_list, check_distance, ground_level):
    object_distance = {
        "up": None,
        "down": None,
        "left": None,
        "right": None
    }
    char_x = 300
    char_y = ground_level - char_physics["coordinates"]["y"]
    char_width = 100
    char_height = 200 

    for object in object_list:
        object_x = -char_physics["coordinates"]["x"] + object["x"]
        object_y = object["y"]
        object_width = object["width"]
        object_height = object["height"]

        if object_x <= char_x + char_width + check_distance and object_x >= char_x + char_width and object_y + object_height >= char_y and object_y <= char_y + char_height:
            object_distance["right"] = object_x - char_x + char_width
        if char_y - check_distance <= object_y + object_height and object_y + object_height <= char_y and object_x + object_width >= char_x and object_x <= char_x + char_width:
            object_distance["up"] = char_y - object_y - object_height
        if char_x - check_distance <= object_x + object_width and object_x + object_width <= char_x and object_y + object_height >= char_y and object_y <= char_y + char_height:
            object_distance["left"] = char_x - object_x + object_width
        if char_y + char_height + check_distance >= object_y and object_y >= char_y + char_height and object_x + object_width >= char_x and object_x <= char_x + char_width:
            object_distance["down"] = object_y - char_y + char_height
    return object_distance
        

# if the thing isnt in the platform coordinates, then freely move right
# but if it is in the coordinates, then don't move right

# for blank in platforms
#     if char coordinates x are >= index[1] and char coords y == index[2]
#     then stop falling until it reaches past index[1] + index[3]