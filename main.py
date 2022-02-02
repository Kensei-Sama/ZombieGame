import sys
import pygame

SZÉLESSÉG, MAGASSÁG = 900, 500
ABLAK = pygame.display.set_mode((SZÉLESSÉG, MAGASSÁG))
pygame.display.set_caption("Operation - Zombie Dash")

FEHÉR = 255, 255, 255
FEKETE = 0, 0, 0
PIROS = 255, 0, 0
ZÖLD = 0, 255, 0
KÉK = 0, 0, 255
TÜRKIZZÖLD = 0, 247, 107

FPS = 60

Játékos = pygame.image.load("")

def ablakleképezés():
    ABLAK.fill((TÜRKIZZÖLD))
    pygame.display.update()


def main():
    képfrissítés = pygame.time.Clock()
    futtatás = True
    while futtatás:
        képfrissítés.tick(FPS)
        for eseményellnőrzés in pygame.event.get():
            if eseményellnőrzés.type == pygame.QUIT:
                futtatás = False

        ablakleképezés()

    pygame.QUIT()

if __name__ == "__main__":
    main()
