import pygame
import sys
import random

user_input = int(input("Wie viele Pixel soll das Spiel breit und hoch sein? "))
pygame.init()
screen = pygame.display.set_mode((800, 800))
FPS = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 100)

field = [[0 for col in range(user_input)] for row in range(user_input)]

field2 = [[0 for col in range(user_input)] for row in range(user_input)]


def randomgenerate():
    for i in range(len(field)):
        for x in range(len(field[0])):
            field[i][x] = random.randint(0, 1)


randomgenerate()


def drawField():
    for i in range(len(field)):
        for x in range(len(field[0])):
            if field[i][x] == 0:
                pygame.draw.rect(screen, (255, 255, 255), (
                    (800 / user_input) * i, (800 / user_input) * x, (800 / user_input), (800 / user_input)))
            else:
                pygame.draw.rect(screen, (0, 0, 0), (
                    (800 / user_input) * i, (800 / user_input) * x, (800 / user_input), (800 / user_input)))


def nextGeneration():
    for i in range(len(field)):
        for x in range(len(field[0])):

            cells = countCells(i, x)

            if field[i][x] == 0:
                if cells == 3:
                    field2[i][x] = 1
            else:
                if cells == 2 or cells == 3:
                    field2[i][x] = 1
                else:
                    field2[i][x] = 0
    for i in range(len(field)):
        for x in range(len(field[0])):
            field[i][x] = field2[i][x]


def countCells(i, x):
    count = 0
    if field[(i - 1 + user_input) % user_input][(x + user_input - 1) % user_input] == 1:
        count += 1
    if field[(i - 1 + user_input) % user_input][(x + user_input) % user_input] == 1:
        count += 1
    if field[(i - 1 + user_input) % user_input][(x + 1 + user_input) % user_input] == 1:
        count += 1
    if field[(i + user_input) % user_input][(x - 1 + user_input) % user_input] == 1:
        count += 1
    if field[(i + user_input) % user_input][(x + 1 + user_input) % user_input] == 1:
        count += 1
    if field[(i + 1 + user_input) % user_input][(x - 1 + user_input) % user_input] == 1:
        count += 1
    if field[(i + 1 + user_input) % user_input][(x + user_input) % user_input] == 1:
        count += 1
    if field[(i + 1 + user_input) % user_input][(x + 1 + user_input) % user_input] == 1:
        count += 1
    return count


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.USEREVENT:
            nextGeneration()
    drawField()
    pygame.display.update()
    FPS.tick(120)
