import pygame
import os

FPS = 60

WIDTH, HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)
TABLE = pygame.transform.scale(
            pygame.image.load(os.path.join("Assets", "pingpongtable.jpg"))
            , (WIDTH, HEIGHT))

def draw_window():

    WINDOW.blit(TABLE, (0,0))

    pygame.display.update()


def main():

    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        draw_window()



if __name__ == "__main__":
    main()