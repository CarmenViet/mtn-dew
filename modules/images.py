import pygame
import os

# Characters
shoellieila_image = pygame.image.load(os.path.join('assets','characters','shoellieila.png'))
shoellieila_image = pygame.transform.scale(shoellieila_image, (100,200))
jollibee_image = pygame.image.load(os.path.join('assets','characters','jollibee.png'))
jollibee_image = pygame.transform.scale(jollibee_image, (100,200))
susan_image = pygame.image.load(os.path.join('assets','characters','susan.png'))
susan_image = pygame.transform.scale(susan_image, (100,200))
richard_image = pygame.image.load(os.path.join('assets','characters','richard.png'))
richard_image = pygame.transform.scale(richard_image, (100,200))
dance_rich_image = pygame.image.load(os.path.join('assets','characters','dance rich.png'))
dance_rich_image = pygame.transform.scale(dance_rich_image, (100, 200))
# Screens
battle_image = pygame.image.load(os.path.join('assets','screens','battle.png'))
intro_image = pygame.image.load(os.path.join('assets','screens','intro.png'))
win_image = pygame.image.load(os.path.join('assets', 'screens', 'win_screen.png'))

# Stages
neighbor1_image = pygame.image.load(os.path.join('assets','stages','neighbor1.png'))
neighbor2_image = pygame.image.load(os.path.join('assets', 'stages', 'neighbor2.png'))
boss_house_image = pygame.image.load(os.path.join('assets', 'stages', 'boss_house.png'))
indoor_image = pygame.image.load(os.path.join('assets', 'stages', 'indoor.png'))

box = pygame.image.load(os.path.join('assets', 'textbox.png'))
options = pygame.image.load(os.path.join('assets', 'options.png'))
crown = pygame.image.load(os.path.join('assets', 'crown.png'))
crown = pygame.transform.scale(crown, (170, 170))
dance_options = pygame.image.load(os.path.join('assets', 'dance_card.png'))