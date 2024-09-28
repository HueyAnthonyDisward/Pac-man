import pygame
import sys

pygame.init()

WIDTH,HEIGHT = 640,600
TILE_SIZE = 40

BLACK = (0,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
RED = (255,0,0)
WHITE = (255,255,255)

MAP = [
    "1111111111111111",
    "1          G   1",
    "1 1111 111111  1",
    "1 1    1    1  1",
    "1 1 1111 1111  1",
    "1 1 1       1  1",
    "1   1  111  1  1",
    "111 1   P    111",
    "1   1  111  1  1",
    "1 1 1       1  1",
    "1 1 1111 1111  1",
    "1 1    1  G 1  1",
    "1 1111 111111  1",
    "1     G        1",
    "1111111111111111",
]
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pac-man")

def draw_map():
    for y, row in enumerate(MAP):
        for x, char in enumerate(row):
            if char == "1":
                pygame.draw.rect(screen, BLUE, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            elif char == "P":
                pygame.draw.circle(screen, YELLOW, (x * TILE_SIZE + TILE_SIZE // 2, y * TILE_SIZE + TILE_SIZE // 2), TILE_SIZE // 2)
            elif char == "G":
                pygame.draw.circle(screen, RED, (x * TILE_SIZE + TILE_SIZE // 2, y * TILE_SIZE + TILE_SIZE // 2), TILE_SIZE // 2)
            elif char == " ":
                pygame.draw.circle(screen, WHITE, (x * TILE_SIZE + TILE_SIZE // 2, y * TILE_SIZE + TILE_SIZE // 2), TILE_SIZE // 8)

def main():
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
        screen.fill(BLACK)
        draw_map()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    sys.exit()

main()

"""
Thành viên nhóm:
Nguyễn Trung Hiếu - 22110138
Lê Hoàng Bảo Phúc - 22110200
Lý Quang Vinh - 22110267
Link video: https://drive.google.com/file/d/1AQyhR4vtpkGA-_Gj6lkYM0CAgHiQFCl0/view?usp=sharing
"""