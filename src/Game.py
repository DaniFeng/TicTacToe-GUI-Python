import pygame
import Board


def mouse_in_bounds(index, loc, mouse):
    return loc[index] < mouse[index] < loc[index] + 160


pygame.init()

oImg = pygame.image.load('o.png')
xImg = pygame.image.load('x.png')

imageLocations = [[(75, 75), (260, 75), (440, 75)],
                  [(75, 260), (260, 260), (440, 260)],
                  [(75, 440), (260, 440), (440, 440)]]

#create game
gameDisplay = pygame.display.set_mode((675, 675))
pygame.display.set_caption("Tic Tac Toe")
gameDisplay.fill([255, 255, 255])

clock = pygame.time.Clock()

board = Board.Board()

while not board.game_over():
    for event in pygame.event.get():
        print(event)

    mouse = pygame.mouse.get_pos()
    for imageLocRow in imageLocations:
        for loc in imageLocRow:
            if mouse_in_bounds(0, loc, mouse) and mouse_in_bounds(1, loc, mouse):
                if pygame.mouse.get_pressed()[0] == 1:
                        gameDisplay.blit(oImg, loc)

    pygame.display.update()
    clock.tick(60)

