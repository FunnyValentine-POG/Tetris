import time
from dataclasses import dataclass
import pygame, sys
from pygame import font
from pygame.locals import *
import random as rd
from pygame.time import Clock

global screen
pygame.init()
width, columns, rows = 400, 10, 20
distance = width // columns
height = distance*rows
speed = 800
score = 0
level = 1
#tạo lưới cho giao diện 
grid = [0]*columns*rows

font = pygame.font.SysFont("comicsans", 40)
text = font.render("Game Over !", True, (255, 0, 0))

def gameover():
	for column in range(columns):			
		if (grid[column]) > 0:
			screen.fill((0,0,0))		
			screen.blit(text,(width//2 - text.get_width()//2,200))

#load picture 
picture = []
for n in range(8):
    picture.append(pygame.transform.scale(pygame.image.load(f'T_0/T_{n}.jpg'),(distance,distance)))

# tạo khung (màng hình) trò chơi 
screen = pygame.display.set_mode([width,height])
pygame.display.set_caption('Tetris Game')

#tạo sự kiện 
tetroromino_down = pygame.USEREVENT +1
speedup = pygame.USEREVENT +2
pygame.time.set_timer(tetroromino_down,speed)
pygame.time.set_timer(speedup,5000)
pygame.key.set_repeat(600,80) #nhan key #ben trai la delay, ben phai la interval (key_press)

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
    column : int = 1 # tọa độ (vị trí xuất hiện lần đầu)
    
    
    def show(self):
        for n, color in enumerate(self.tetro):
            if color > 0 :
                x = (self.column + n % 4) * distance
                y = (self.row + n // 4) * distance
                screen.blit(picture[color],(x,y))

    def check_grid(self,r,c):
        for n, color in enumerate(self.tetro):
            if color>0:
                rs = r + n//4
                cs = c + n%4
                if cs<0 or rs >=rows or cs >=columns or grid[rs * columns +cs]>0:
                    return False
        return True

    def update(self,r,c):
        if self.check_grid(self.row + r, self.column +c):
            self.row += r
            self.column += c
            return True
        return False
    def Rotation(self): #xoay cac khoi
        savetetro = self.tetro.copy()
        for n, color in enumerate(savetetro):
            self.tetro[(2-(n%4))*4+(n//4)] = color
        if not self.check_grid(self.row, self.column):
            self.tetro = savetetro.copy() 


character = tetroromino(rd.choice(tetrorominos))

def game_loop():
    for n,color in enumerate(character.tetro):
        if color > 0:
            grid[(character.row + n//4)*columns +(character.column+n%4)]=color

def clear_rows():
    fullrows = 0
    for row in range(rows):
        for column in range(columns):
            if grid[row * columns+column] == 0:
                break
        else:
            del grid[row * columns : row * columns+column]
            grid[0:0] = [0]*columns
            fullrows +=1
    return fullrows*100   #set diem la 100 diem

def drawGrid():
    blockSize = 40 
    for x in range(0, width, blockSize):
        for y in range(0, height, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, (128,128,128), rect, 1)


status = True
while status:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False
        if event.type == tetroromino_down:
            if not character.update(1,0):
                game_loop()
                character = tetroromino(rd.choice(tetrorominos))
                score += clear_rows()
            gameover()
        if event.type == speedup:
            if score % 500 == 0 and score !=0:
                speed = int (speed * 0.7)
                pygame.time.set_timer(tetroromino_down,speed)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character.update(0,-1)
            if event.key == pygame.K_RIGHT:
                character.update(0,1)
            if event.key == pygame.K_DOWN:
                character.update(1,0)
            if event.key == pygame.K_UP:
                character.Rotation()
    # background color
    screen.fill((0,0,0))
    drawGrid()
    character.show()
    textsurface = pygame.font.SysFont('ComicSans',30).render("Score: "f'{score:,}',True,(255,255,255))
    screen.blit(textsurface,(width//2 - textsurface.get_width()//2,10))
    #duyệt các khối màu
    for n, color in enumerate(grid):
        if color > 0:
            x = n % columns * distance
            y = n // columns * distance
            screen.blit(picture[color],(x,y))
    pygame.display.flip()

pygame.quit()



