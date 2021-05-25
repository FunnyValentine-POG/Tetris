import time
from dataclasses import dataclass
import pygame, sys
from pygame import font
from pygame.locals import *
import random as rd
from pygame.time import Clock

pygame.init()
width, columns, rows = 400, 10, 20
distance = width // columns
height = distance*rows

#tạo lưới cho giao diện 
grid = [0]*columns*rows

#load picture 
picture = []
for n in range(8):
    picture.append(pygame.transform.scale(pygame.image.load(f'T_0/T_{n}.jpg'),(distance,distance)))

# tạo khung (màng hình) trò chơi 
screen = pygame.display.set_mode([width,height])
pygame.display.set_caption('Tetris Game')

# create event
tetroromino_down = pygame.USEREVENT + 1
pygame.time.set_timer(tetroromino_down,500)
# tetrorominos: O, I, J, L, S, Z, T
tetrorominos = [
                [0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0], # O
                [0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0], # I
                [0,0,0,0,3,3,3,0,0,0,3,0,0,0,0,0], # J
                [0,0,4,0,4,4,4,0,0,0,0,0,0,0,0,0], # L
                [0,5,5,0,5,5,0,0,0,0,0,0,0,0,0,0], # S
                [6,6,0,0,0,6,6,0,0,0,0,0,0,0,0,0], # Z
                [0,0,0,0,7,7,7,0,0,7,0,0,0,0,0,0]  # T
                ] 

# tạo lớp và định nghĩa hàm
@dataclass
class tetroromino():
    tetro : list 
    row : int = 0
    column : int = 5 # tọa độ (vị trí xuất hiện lần đầu)
    
    
    def show(self):
        for n, color in enumerate(self.tetro):
            if color > 0 :
                x = (self.column + n % 4) * distance
                y = (self.column + n // 4) * distance
                screen.blit(picture[color],(x,y))
                
    def update(self,r,c):
        self.row += r
        self.column += c
                
character = tetroromino(tetrorominos[2])


status = True
while status:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False
        if event.type == tetroromino_down:
            character.update(1,0)
    # background color
    screen.fill((128,128,128))
    character.show()
    #duyệt các khối màu
    for n, color in enumerate(grid):
        if color > 0:
            x = n % columns * distance
            y = n // columns * distance
            screen.blit(picture[color],(x,y))
    pygame.display.flip()
pygame.quit()


