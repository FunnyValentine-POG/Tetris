import pygame, sys
from pygame import font
from pygame.locals import *
import random as rd


pygame.font.init()

s_width = 800
s_height = 700
play_width = 300  #chieu rong khung game   chieu rong 
play_height = 600  # chieu dai khung game
block_size = 30

top_left_x = (s_width - play_width) // 2 #khu vuc choi cua game
top_left_y = s_height - play_height


# Hinh dang khoi block

S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# index dua tren shapes

class Piece(object):
    rows = 20  # y
    columns = 10  # x
 
    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)] # index dua tren shapes cua 
        self.rotation = 0  # dieu chinh sau bang nut mui ten len 

def create_grid(locked_positions={}):
    grid = [[(0,0,0) for x in range(10)] for x in range(20)] #tuong trung cho 10 mau, 20 row 
 
    for i in range(len(grid)):  #20 row
        for j in range(len(grid[i])):
            if (j,i) in locked_positions:
                c = locked_positions[(j,i)]
                grid[i][j] = c
    return grid

def get_shape():
      return rd.choice(shapes)  #chon shapes rot xuong 

def draw_grid(surface,grid):
      

      for i in range(len(grid)):
            for j in range(len(grid[i])):
                  pygame.draw.rect(surface,grid[i][j],(top_left_x+j*block_size,top_left_y+i*block_size,block_size,block_size),0)
      
      pygame.draw.rect(surface,(255,0,0),(top_left_x,top_left_y,play_width,play_height),4) #ve khung cua game (mau do)
      
      

def draw_window(surface,grid):
      surface.fill((0,0,0))  #fill mau nen game (default la mau den) 

      pygame.font.init()
      font = pygame.font.sysFont('comicsans',60) #chinh font game 
      label = font.render('Tetris', 1, (255,255,255)) #ten game la Tetris

      surface.blit(label,(top_left_x+play_width/2)) #chinh chu Tetris chinh giua game

      draw_grid(surface,grid)
      pygame.display.update()