import pygame
from modules.render import *
from modules.movement import *
from modules.images import *
import csv
pygame.font.init()

font = pygame.font.SysFont('comicsans', 40)
white = (255, 255, 255)
black = (0, 0, 0)

level_two_platforms = []
with open('./assets/platforms/stage_two_platforms.csv') as dragonfruit:
    durian = csv.reader(dragonfruit)
    row_num = 0
    for row in durian:
        if row_num > 0:
            level_two_platforms.append({
                "x": int(row[1]),
                "y": int(row[2]),
                "width": int(row[3]),
                "height": int(row[4])
            })
        row_num += 1

level_two_obstacles = []

with open('./assets/obstacles/stage_two_obstacles.csv') as strawberry:
    mango = csv.reader(strawberry)
    row_num = 0
    for row in mango:
        if row_num > 0:
            level_two_obstacles.append({
                "x": int(row[1]),
                "y": int(row[2]),
                "width": int(row[3]),
                "height": int(row[4])
            })
        row_num += 1

def show_level_two(screen, clock):
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

        render_stage(screen, char_physics["coordinates"], neighbor2_image)
        render_protag(screen, char_physics["coordinates"], ground_level=500)
        render_neighbor(screen, char_physics["coordinates"], susan_image, neighbor_base_coordinates=[1706, 500])
        
        handle_jumping(char_physics)

        for platform in level_two_platforms:
            pygame.draw.rect(screen, white, (-char_physics["coordinates"]["x"] + platform["x"], platform["y"], platform["width"], platform["height"]))
        
        for obstacle in level_two_obstacles:
            pygame.draw.rect(screen, black, (-char_physics["coordinates"]["x"] + obstacle["x"], obstacle["y"], obstacle["width"], obstacle["height"]))

        if char_physics["coordinates"]["x"] <= 1273:
            handle_movement(char_physics["coordinates"])
            handle_jump_press(char_physics)    
        else:

            #her first box

            if first_box == True:
                screen.blit(box, (0, 0))
                question = font.render("Howdy. I'm Susan McAllister, pleased to meet you!", 1, white)
                screen.blit(question, (50,50))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #pos = pygame.mouse.get_pos()
                        first_box = False
                    
            elif first_box == False:

                #your response options

                if response == "True":
                    screen.blit(options, (0, 0))
                    choice1 = font.render("Hello Susan. I'm Shoellieila! Why do you live by the mountains?", 1, white)
                    choice2 = font.render("Nice to meet you! I'm Shoellieila. Perchance, are you married? ", 1, white)
                    choice3 = font.render("yo suzie, do u have any games on ur phone?", 1, white)

                    #you choosing a response

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
                
                
                #her responses
                elif response == "one":
                    screen.blit(box, (0, 0))
                    response1 = font.render("Well, I'd tell you, but then I'd have to kill you.", 1, white)
                    screen.blit(response1, (50, 50))
                    response1again = font.render("Haha, kidding. I like the peace and quiet. I have to get going.", 1, white)
                    screen.blit(response1again, (50, 130))
                    response1again2pm = font.render("It was nice meeting you!", 1, white)
                    screen.blit(response1again2pm, (50, 210))
                    move = False
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            move = True
                    if move == True:
                        break
                elif response == "two":
                    screen.blit(box, (0, 0))
                    response2 = font.render("I'm a widow.", 1, white)
                    screen.blit(response2, (50, 50))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pygame.quit()
                elif response == "three":
                    screen.blit(box, (0, 0))
                    response3 = font.render(". . .", 1, white)
                    screen.blit(response3, (50, 50))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pygame.quit()
            

        pygame.display.update()
        clock.tick(60)
        