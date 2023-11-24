import pygame
import os

# Characters
shoellieila_image = pygame.image.load(os.path.join('assets','characters','shoellieila.png'))
shoellieila_image = pygame.transform.scale(shoellieila_image, (100,200))
jollibee_image = pygame.image.load(os.path.join('assets','characters','jollibee.png'))
jollibee_image = pygame.transform.scale(jollibee_image, (100,200))
susan_image = pygame.image.load(os.path.join('assets','characters','susan.png'))
richard_image = pygame.image.load(os.path.join('assets','characters','richard.png'))
dog_image = pygame.image.load(os.path.join('assets','characters','dog.png'))
dance_rich_image = pygame.image.load(os.path.join('assets','characters','dance rich.png'))

# Screens
battle_image = pygame.image.load(os.path.join('assets','screens','battle.png'))
intro_image = pygame.image.load(os.path.join('assets','screens','intro.png'))

# Stages
neighbor1_image = pygame.image.load(os.path.join('assets','stages','neighbor1.png'))