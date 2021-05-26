import time
from dataclasses import dataclass
import pygame, sys
from pygame import font
from pygame.locals import *
import random as rd
from pygame import mixer

global screen
status = True
pygame.init()
width, columns, rows = 400, 10, 20
distance = width // columns
height = distance*rows
speed, score, level, level0 = 1000, 0, 1, 0

#tạo lưới cho giao diện 
grid = [0]*columns*rows

#BGM
music = mixer.music.load('BGM/Tetris.wav')
mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

#load picture 
picture = []
for n in range(8):
    picture.append(pygame.transform.scale(pygame.image.load(f'T_0/T_{n}.jpg'),(distance,distance)))

# tạo khung (màng hình) trò chơi 
screen = pygame.display.set_mode([width,height])
pygame.display.set_caption('Tetris Game')

#tạo sự kiện 
tetroromino_down = pygame.USEREVENT +1
#speedup = pygame.USEREVENT +2

pygame.time.set_timer(tetroromino_down,speed)
#pygame.time.set_timer(speedup,5000)

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
    column : int = 4 # tọa độ (vị trí xuất hiện lần đầu)
    
    
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
    return fullrows**2*100   #set diem la 100 diem

def clear_all_rows():
    fullrows = 0
    for row in range(rows):
        for column in range(columns):
            if grid[row * columns+column] == 0:
                del grid[row * columns : row * columns+column]

def drawGrid():
    blockSize = 40 
    for x in range(0, width, blockSize):
        for y in range(0, height, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, (128,128,128), rect, 1)
    
    
def button(x, y, width, height,ahrefs, action):
    mouse = pygame.mouse.get_pos()
    bt = pygame.transform.scale(pygame.image.load(f'button/{ahrefs}.png'),(width,height))
    clicked = pygame.mouse.get_pressed()
    if x <= mouse[0] <= x + width and y <= mouse[1] <= y + height:
        #pygame.transform.scale(pygame.image.load(f'button/play.png'),(width,height))
        if clicked[0] and action != None:
            action()
    else:
        pygame.transform.scale(pygame.image.load(f'button/play.png'),(width,height))
    screen.blit(bt ,(x,y))
def print_text(text, size, color, x, y):
    
    font = pygame.font.SysFont("comicsans", size)
    texts = font.render(text, True, color)
    x = x - texts.get_width() // 2
    screen.blit(texts, (x,y))
def gameover():
    over = False
    for column in range(columns):
        if (grid[column]) > 0:
            over = True
            break
        
    while over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                over = False
                global status
                status = False  
        bk = pygame.image.load(f'Game_background/B_3.jpg')    
        screen.blit(bk,(0,0))
        button((width//2 - 100), height*0.6 , 200, 89,'restart', Menu)
        #status , over = True, False
        #score, speed, level, level0 = 0, 1000, 1, 0
        #clear_all_rows()
        pygame.display.update()

pause = False

def Resume():
    global pause
    pause = False

def Pause():
    global pause, status
    pause = True
    while pause:        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pause = False
                status = False        
        bk = pygame.image.load(f'Game_background/B_2.jpg')    
        screen.blit(bk,(0,0))
        button((width//2 - 100), height*0.6 , 200, 89,'pause', Resume)
        pygame.display.update()

def Play():
    global status , score, speed, level, level0, character
    while status:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = False
            if event.type == tetroromino_down:
                if not character.update(1,0):
                    game_loop()
                    score += clear_rows()
                    if score > 0 and score // 500 >= level and level0 != score:
                        speed = int (speed * 0.9)
                        pygame.time.set_timer(tetroromino_down,speed)
                        level = score // 500 + 1
                        level0 = score
                    character = tetroromino(rd.choice(tetrorominos))
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    character.update(0,-1)
                if event.key == pygame.K_RIGHT:
                    character.update(0,1)
                if event.key == pygame.K_DOWN:
                    character.update(1,0)
                if event.key == pygame.K_UP:
                    character.Rotation()
                if event.key == pygame.K_SPACE:
                    Pause()
    
        gameover()
        # background color
        screen.fill((0,0,0))
        drawGrid()
        character.show()
        textsurface = pygame.font.SysFont('ComicSans',40).render("Score: "f'{score:,}',True,(255,255,255))
        screen.blit(textsurface,(width//2 - textsurface.get_width()//2,30))
        textsurface = pygame.font.SysFont('ComicSans',30).render("Level: "f'{level:,}',True,(255,255,255))
        screen.blit(textsurface,(width//2 - textsurface.get_width()//2,5))
        #duyệt các khối màu
        for n, color in enumerate(grid):
            if color > 0:
                x = n % columns * distance
                y = n // columns * distance
                screen.blit(picture[color],(x,y))
        pygame.display.flip()

def Menu():
    global status
    while status:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = False
            else:
                bk = pygame.image.load(f'Game_background/B_1.jpg')    
                screen.blit(bk,(0,0))
                button((width//2 - 100), height*0.5, 200, 89,'play', Play)
            
        pygame.display.update()
#Play()

Menu()

pygame.quit()



