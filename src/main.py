import pygame
import os
import time
import random
import utils

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Load images
RED_SPACE_SHIP = pygame.image.load(os.path.join(utils.get_assets_folder_path(), "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join(utils.get_assets_folder_path(), "pixel_ship_red_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join(utils.get_assets_folder_path(), "pixel_ship_blue_small.png"))

# Player ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join(utils.get_assets_folder_path(), "pixel_ship_yellow.png"))

# Lasers
RED_LASER = pygame.image.load(os.path.join(utils.get_assets_folder_path(), "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join(utils.get_assets_folder_path(), "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join(utils.get_assets_folder_path(), "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join(utils.get_assets_folder_path(), "pixel_laser_yellow.png"))

# Background
BG = pygame.image.load(os.path.join(utils.get_assets_folder_path(), "background-black.png"))


print("done")


