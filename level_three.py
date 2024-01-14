import pygame
from modules.render import *
from modules.movement import *
from modules.images import *
import csv
pygame.font.init()
pygame.mixer.init()

font = pygame.font.SysFont('comicsans', 40)
white = (255, 255, 255)
black = (0, 0, 0)

level_three_platforms = []

with open('./assets/platforms/stage_three_platforms.csv') as cherry:
    blueberry = csv.reader(cherry)
    row_num = 0
    for row in blueberry:
        if row_num > 0:
            level_three_platforms.append({
                "x": int(row[1]),
                "y": int(row[2]),
                "width": int(row[3]),
                "height": int(row[4])
            })
        row_num += 1

level_three_obstacles = []

with open('./assets/obstacles/stage_three_obstacles.csv') as pear:
    watermelon = csv.reader(pear)
    row_num = 0
    for row in watermelon:
        if row_num > 0:
            level_three_obstacles.append({
                "x": int(row[1]),
                "y": int(row[2]),
                "width": int(row[3]),
                "height": int(row[4])
            })
        row_num += 1

def show_level_three_outdoors(screen, clock):
    char_physics = {
        "coordinates": {
            "x": 0,
            "y": 0
        },
        "jump_velocity": 0
    }

    intro_box = "active"
    meltingpoint = os.path.join('assets', 'meltingpoint.mp3')
    pygame.mixer.music.load(meltingpoint)
    outside_volume = 0.1
    pygame.mixer.music.set_volume(outside_volume)
    pygame.mixer.music.play(loops = -1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        render_stage(screen, char_physics["coordinates"], boss_house_image)
        render_protag(screen, char_physics["coordinates"], ground_level=400)
        handle_jumping(char_physics)

        if intro_box == "active":
            screen.blit(box, (0,0))
            intro = font.render("Woah, I can hear the music blasting from that house.", 1, white)
            screen.blit(intro, (50,50))
            intro2 = font.render("Whoever lives in there must be exciting!", 1, white)
            screen.blit(intro2, (50, 130))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    intro_box = "inactive"

        
        if char_physics["coordinates"]["x"] <= 900 and intro_box == "inactive":
            handle_movement(char_physics["coordinates"])
            handle_jump_press(char_physics)
        else:
            if char_physics["coordinates"]["x"] > 900:
                screen.blit(box, (0, 0))
                question = font.render("The door is ajar. Shall we go in?", 1, white)
                screen.blit(question, (50,50))
                enter = False
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        enter = True
                if enter == True:
                    break



        pygame.display.update()
        clock.tick(60)

def show_level_three_indoors(screen, clock):
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
                
        render_stage(screen, char_physics["coordinates"], indoor_image)
        render_protag(screen, char_physics["coordinates"], ground_level=400)
        render_neighbor(screen, char_physics["coordinates"], richard_image, neighbor_base_coordinates=[1506, 400])
        handle_jumping(char_physics)

        for platform in level_three_platforms:
            pygame.draw.rect(screen, white, (-char_physics["coordinates"]["x"] + platform["x"], platform["y"], platform["width"], platform["height"]))
        
        for obstacle in level_three_obstacles:
            pygame.draw.rect(screen, black, (-char_physics["coordinates"]["x"] + obstacle["x"], obstacle["y"], obstacle["width"], obstacle["height"]))        

        inside_volume = 1.0
        pygame.mixer.music.set_volume(inside_volume)

        if char_physics["coordinates"]["x"] <= 1043:
            handle_movement(char_physics["coordinates"])
            handle_jump_press(char_physics)

        else:
            if first_box == True:
                screen.blit(box, (0, 0))
                question = font.render("MR. RICHARD? My boss?? You're the one throwing a party???", 1, white)
                screen.blit(question, (50,50))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        first_box = False
                    
            elif first_box == False:

                if response == "True":

                    render_stage(screen, char_physics["coordinates"], indoor_image)
                    render_protag(screen, char_physics["coordinates"], ground_level=400)
                    render_neighbor(screen, char_physics["coordinates"], dance_rich_image, neighbor_base_coordinates=[1506, 400])

                    screen.blit(box, (0, 0))
                    rich_response = font.render("Shoellieila? Ah. You must be my new neighbor.", 1, white)
                    screen.blit(rich_response, (50, 50))
                    rich_question = font.render("Well, this is incredibly awkward for me. To fix this, you must", 1, white)
                    screen.blit(rich_question, (50, 130))
                    rich_proposition = font.render("defeat me in a dance battle, or else you're fired.", 1, white)
                    screen.blit(rich_proposition, (50, 210))

                    move = False
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            move = True
                    if move == True:
                        break

        pygame.display.update()
        clock.tick(60)

def show_level_three_dance(screen, clock):
    char_physics = {
        "coordinates": {
            "x": 0,
            "y": 0
        },
        "jump_velocity": 0
    }
    
    first_box = False
    second_box = False
    third_box = False
    xox = True
    choose = False
    response = "nothing"
    chose = False
    end = False
    clicked = False
    awe = "cool"
    win = False

    boptothetop = os.path.join('assets', 'boptothetop.mp3')
    pygame.mixer.music.load(boptothetop)
    pygame.mixer.music.play(loops = -1)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        if first_box == False:
            render_stage(screen, char_physics["coordinates"], battle_image)
        if xox == True:        
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    first_box = True
                    xox = False

        if first_box == True:
            screen.blit(box, (0, 400))
            words = font.render("You have engaged in a dance battle with your boss Richard!", 1, white)
            screen.blit(words, (50, 450))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    second_box = True
                    first_box = False
        if second_box == True:
            screen.blit(box, (0, 400))
            stats = font.render("Profiles:", 1, white)
            screen.blit(stats, (50, 450))
            richie_stats = font.render("Richard \"Richie\" Richard, Your boss at work, Fashionable(?)", 1, white)
            screen.blit(richie_stats, (50, 530))  
            shoellieila_stats = font.render("Shoellieila, New kid on the block, Mandated corporate worker", 1, white)          
            screen.blit(shoellieila_stats, (50, 610))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    second_box = False
                    third_box = True
        if third_box == True:
            screen.blit(box, (0, 400))
            richie_move = font.render("Richard has started off the battle with a shady glare and", 1, white)
            screen.blit(richie_move, (50, 450))
            richie_move_2 = font.render("the lawnmower (dance)! Who knew he had it in him and", 1, white)      
            screen.blit(richie_move_2, (50, 530))     
            richie_move_3 = font.render("old man body? Highly effective! Critical damage taken!", 1, white) 
            screen.blit(richie_move_3, (50, 610))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    chose = True
                    choose = True
            if chose == True:
                render_stage(screen, char_physics["coordinates"], dance_options)
        if choose == True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = pygame.mouse.get_pos()
                    if 417 > click[0] and click[0] > 98 and 360 > click[1] and click[1] > 114 and clicked == False:
                        response = "one"
                        clicked = True
                    elif 805 > click[0] and click[0] > 473 and 663 > click[1] and click[1] > 425 and clicked == False:
                        response = "two"
                        clicked = True
                    elif 1180 > click[0] and click[0] > 860 and 360 > click[1] and click[1] > 114 and clicked == False:
                        response = "three"
                        clicked = True
        if response == "one" and clicked == True:
            render_stage(screen, char_physics["coordinates"], battle_image)
            screen.blit(box, (0, 400))
            dab = font.render("You have officially established yourself as the lamest person at", 1, white)
            screen.blit(dab, (50, 450))
            dabbed = font.render("this party.", 1, white)
            screen.blit(dabbed, (50, 530))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    end = True
            if end == True:
                break
        elif response == "two":
            render_stage(screen, char_physics["coordinates"], battle_image)
            screen.blit(box, (0, 400))
            choreography = font.render("Little did Richie know, good ol' Shoellieila was in a famous", 1, white)
            screen.blit(choreography, (50, 450))
            choreo = font.render("idol group for two and a half years until your contract expired.", 1, white)
            screen.blit(choreo, (50, 530))
            choreos = font.render("You hit him with some sick dance moves!", 1, white)
            screen.blit(choreos, (50, 610))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    awe = "amazing"
        elif response == "three":
            render_stage(screen, char_physics["coordinates"], battle_image)
            screen.blit(box, (0, 400))
            splits = font.render("You instantly break your legs and your pants rip embarrassingly.", 1, white)
            screen.blit(splits, (50, 450))
            quits = font.render("You leave and run home. Richard didn't fire you, but you end up", 1, white)
            screen.blit(quits, (50, 530))
            quitting = font.render("quitting your job out of pure shame.", 1, white)
            screen.blit(quitting, (50, 610))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    end = True
            if end == True:
                break
        if awe == "amazing":
            screen.blit(box, (0, 400))
            incredible = font.render("Wow. I'm in awe of your talent. I used to be known around", 1, white)
            screen.blit(incredible, (50, 450))
            so_cool = font.render("the block as the dancing king, but I admit that you're better.", 1, white)
            screen.blit(so_cool, (50, 530))
            woah = font.render("I officially declare you to be the best dancer here!", 1, white)
            screen.blit(woah, (50, 610))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    win = True   
            if win == True:
               render_stage(screen, char_physics["coordinates"], win_image)      
               render_protag(screen, char_physics["coordinates"], ground_level=300)
               screen.blit(crown, (265, 225))
        
        pygame.display.update()
        clock.tick(60)

def show_level_three(screen, clock):
    show_level_three_outdoors(screen, clock)
    show_level_three_indoors(screen, clock)
    show_level_three_dance(screen, clock)