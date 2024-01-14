import pygame
from modules.render import *
from modules.movement import *
from modules.images import *
import csv
pygame.font.init()

font = pygame.font.SysFont('comicsans', 40)
white = (255, 255, 255)
black = (0, 0, 0)

level_one_platforms = []

with open('./assets/platforms/stage_one_platforms.csv') as banana:
    orange = csv.reader(banana)
    row_num = 0
    for row in orange:
        if row_num > 0:
            level_one_platforms.append({
                "x": int(row[1]),
                "y": int(row[2]),
                "width": int(row[3]),
                "height": int(row[4])
            })
        row_num += 1

level_one_obstacles = []

with open('./assets/obstacles/stage_one_obstacles.csv') as apple:
    pineapple = csv.reader(apple)
    row_num = 0
    for row in pineapple:
        if row_num > 0:
            level_one_obstacles.append({
                "x": int(row[1]),
                "y": int(row[2]),
                "width": int(row[3]),
                "height": int(row[4])
            })
        row_num += 1

def show_level_one(screen, clock):
    char_physics = {
        "coordinates": {
            "x": 0,
            "y": 0
        },
        "jump_velocity": 0
    }
    
    first_box = True
    response = "True"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        render_stage(screen, char_physics["coordinates"], neighbor1_image)
        render_protag(screen, char_physics["coordinates"], ground_level=400)
        render_neighbor(screen, char_physics["coordinates"], jollibee_image, neighbor_base_coordinates=[3606, 400])

        check_if_touching_obstacle(char_physics, level_one_obstacles, 8, 400)
        can_jump = handle_jumping(char_physics, level_one_platforms, ground_level=400)

        if char_physics["coordinates"]["x"] <= 3053:
            handle_movement(char_physics["coordinates"])
            handle_jump_press(char_physics, can_jump)    

        else:
            if first_box == True:
                screen.blit(box, (0, 0))
                question = font.render("hi!!! i'm jollibee!! whats your favourite fruit?", 1, white)
                screen.blit(question, (50,50))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #pos = pygame.mouse.get_pos()
                        first_box = False
                    
            elif first_box == False:
                if response == "True":
                    screen.blit(options, (0, 0))
                    choice1 = font.render("pineapple", 1, white)
                    choice2 = font.render("tomato", 1, white)
                    choice3 = font.render("maraschino cherry", 1, white)
                    screen.blit(choice1, (50, 40))
                    screen.blit(choice2, (50, 130))
                    screen.blit(choice3, (50, 210))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            click = pygame.mouse.get_pos()
                            #print (click)
                            if 1248 > click[0] and click[0] > 30 and 126 > click[1] and click[1] > 30:
                                response = "one"
                            elif 1248 > click[0] and click[0] > 30 and 204 > click[1] and click[1] > 127:
                                response = "two"
                            elif 1248 > click[0] and click[0] > 30 and 283 > click[1] and click[1] > 207:
                                response = "three"
                elif response == "one":
                    screen.blit(box, (0, 0))
                    response1 = font.render("not my thing... uh nice to meet you i guess... (awkward silence)", 1, white)
                    screen.blit(response1, (50, 50))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pygame.quit()
                elif response == "two":
                    screen.blit(box, (0, 0))
                    response2 = font.render("you disgust me get out of my face??", 1, white)
                    screen.blit(response2, (50, 50))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pygame.quit()
                elif response == "three":
                    screen.blit(box, (0, 0))
                    response3 = font.render("oh my god me too lets be the best of friends forever!!!", 1, white)
                    screen.blit(response3, (50, 50))
                    response3again = font.render("well it was nice to meet you! cya around!!", 1, white)
                    screen.blit(response3again, (50, 130))
                    x = False
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            x = True
                    if x == True:
                        break

        pygame.display.update()
        clock.tick(60)


