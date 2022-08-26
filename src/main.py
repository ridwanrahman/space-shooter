import os
import pygame
import time
import random
import utils

from Ship import Ship

pygame.font.init()

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Load images
RED_SPACE_SHIP = pygame.image.load(os.path.join(utils.get_assets_folder_path(), "assets/pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join(utils.get_assets_folder_path(), "assets/pixel_ship_red_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join(utils.get_assets_folder_path(), "assets/pixel_ship_blue_small.png"))

# Player ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join(utils.get_assets_folder_path(), "assets/pixel_ship_yellow.png"))

# Lasers
RED_LASER = pygame.image.load(os.path.join(utils.get_assets_folder_path(), "assets/pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join(utils.get_assets_folder_path(), "assets/pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join(utils.get_assets_folder_path(), "assets/pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join(utils.get_assets_folder_path(), "assets/pixel_laser_yellow.png"))

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join(utils.get_assets_folder_path(), "assets/background-black.png")), (WIDTH, HEIGHT))


def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 25)

    ship = Ship(300, 650)

    clock = pygame.time.Clock()

    def redraw_window():
        """Draws the background image and writes level
        """
        WIN.blit(BG, (0, 0))
        # draw text
        lives_label = main_font.render(f"Level: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH-level_label.get_width() - 10, 10))

        ship.draw(WIN)

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


if __name__ == '__main__':
    """38:43 in the tutorial
    https://www.youtube.com/watch?v=Q-__8Xw9KTM&t=876s
    """
    main()

