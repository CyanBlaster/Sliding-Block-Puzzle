import sys
import pygame
import datetime
import math
import pygame.freetype

pygame.init()


def ZeroField(n):
    return [[0] * n for i in range(n)]


def createVerticalLine(board, x, y, length):
    if(length < 10):
        for i in range(length):
            board[x][y + i] = 3


def main():
    width = 501
    height = 501
    screen = pygame.display.set_mode((width, height))
    running = True
    xIdx = 2
    yIdx = 2
    playmode = False
    board = ZeroField(10)
    select = False
    while running:
        pygame.display.flip()
        screen.fill((0, 0, 0))
        for i in range(0, 10):
            pygame.draw.line(screen, (0, 0, 255), (i * 500/10, 0), (i * 500/10, 500))
            pygame.draw.line(screen, (0, 0, 255), (0, i * 500/10), (500, i * 500/10))
        
        

        
        for y in range(10):
            for x in range(10):
                if(board[x][y] == 3):
                    pygame.draw.rect(screen, (255, 0, 255), (x * 50 + 1, y * 50 + 1, 49, 49))
                if(board[x][y] == 2):
                    pygame.draw.rect(screen, (0, 255, 0), (x * 50 + 1, y * 50 + 1, 49, 49))
                if(board[x][y] == 1):
                    pygame.draw.rect(screen, (0, 0, 255), (x * 50 + 1, y * 50 + 1, 49, 49))
        
        if(playmode == False):
            pygame.draw.rect(screen, (255, 255, 255), (xIdx * 50 + 1, yIdx * 50 + 1, 49, 49))
        else:
            pygame.draw.rect(screen, (255, 255, 255), (xIdx * 50 + 1, yIdx * 50 + 1, 49, 49))
            pygame.draw.rect(screen, (0, 0, 0), (xIdx * 50 + 2, yIdx * 50 + 2, 47, 47))

        
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False
            elif events.type == pygame.KEYDOWN:
                if events.key == pygame.K_LEFT:
                    xIdx -= 1
                    if(xIdx == -1):
                        xIdx = 0
                elif events.key == pygame.K_RIGHT:
                    xIdx += 1
                    if(xIdx == 10):
                        xIdx = 9
                elif events.key == pygame.K_UP:
                    yIdx -= 1
                    if(yIdx == -1):
                        yIdx = 0
                elif events.key == pygame.K_DOWN:
                    yIdx += 1
                    if(yIdx == 10):
                        yIdx = 9
                elif events.key == pygame.K_d:
                    if(playmode == False):
                        for y in range(10):
                            for x in range(10):
                                if(board[x][y] == 2):
                                    pygame.draw.rect(screen, (0, 0, 0), (x * 50 + 1, y * 50 + 1, 49, 49))
                                    board[x][y] = 0
                        board[xIdx][yIdx] = 2
                elif events.key == pygame.K_f:
                    if(playmode == False):
                        for y in range(10):
                            for x in range(10):
                                if(board[x][y] == 1):
                                    pygame.draw.rect(screen, (0, 0, 0), (x * 50 + 1, y * 50 + 1, 49, 49))
                                    board[x][y] = 0
                        board[xIdx][yIdx] = 1
                elif events.key == pygame.K_s:
                     if(playmode == False):
                        board[xIdx][yIdx] = 3
                elif events.key == pygame.K_a:
                             if(playmode == False):
                                if(board[xIdx][yIdx] == 3):
                                    pygame.draw.rect(screen, (0, 0, 0), (xIdx * 50 + 1, yIdx * 50 + 1, 49, 49))
                                    board[xIdx][yIdx] = 0
                elif events.key == pygame.K_p:
                    if(playmode):
                        playmode = False
                        select = False
                    else:
                        playmode = True
                
                elif events.key == pygame.K_SPACE:
                    if(playmode):
                        if(select == True):
                            select = False
                            for y in range(10):
                               for x in range(10):
                                   if(board[x][y] == 1):
                                      pygame.draw.rect(screen, (0, 0, 0), (x * 50 + 1, y * 50 + 1, 49, 49))
                                      board[x][y] = 0
                            board[xIdx][yIdx] = 1
                        else:
                            if(board[xIdx][yIdx] == 1):
                               select = True
                        
main()