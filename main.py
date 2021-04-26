import pygame
import os
from Player import Player

FPS = 60

VEL = 5

WIDTH, HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)
TABLE = pygame.transform.scale(
            pygame.image.load(os.path.join("Assets", "pingpongtable.jpg"))
            , (WIDTH, HEIGHT))

PLAYER_WIDTH, PLAYER_HEIGHT = 10, 100

PLAYER_ONE = pygame.Rect(
                            50, HEIGHT//2 + PLAYER_HEIGHT//2 #x y
                            , PLAYER_WIDTH, PLAYER_HEIGHT
                        )

PLAYER_TWO = pygame.Rect(   
                            WIDTH - 50, HEIGHT//2 + PLAYER_HEIGHT//2 #x, y
                            , PLAYER_WIDTH, PLAYER_HEIGHT
                            )


KEY_BINDINGS = {
    "player_one": {
        "Up": pygame.K_w, 
        "Down": pygame.K_s
        },
    "player_two": {
        "Up": pygame.K_UP, 
        "Down": pygame.K_DOWN
        }
}

def draw_window(player_one, player_two):

    WINDOW.blit(TABLE, (0,0))
    pygame.draw.rect(WINDOW, BLACK, player_one)
    pygame.draw.rect(WINDOW, BLACK, player_two)

    pygame.display.update()


def main():

    player_one = Player(PLAYER_ONE, VEL, KEY_BINDINGS["player_one"])
    player_two = Player(PLAYER_TWO, VEL, KEY_BINDINGS["player_two"])

    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        keys_pressed = pygame.key.get_pressed()
        player_one.movement(keys_pressed, HEIGHT)
        player_two.movement(keys_pressed, HEIGHT)

        draw_window(player_one.player, player_two.player)



if __name__ == "__main__":
    main()