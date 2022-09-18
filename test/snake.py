import math
from multiprocessing import BoundedSemaphore
import random
import pygame, sys
from pygame.locals import *
import random as r

pygame.init()
pygame.font.init()
BLACK = (0, 0, 0)
green=(0,255,0)
red=(255,0,0)
FPS = 12
DIS = pygame.display.set_mode((1000, 1000))
FramePerSec = pygame.time.Clock()


class apple:
    def __init__(self):
        self.pos=[r.randint(0,20),r.randint(0,20)]

    
    
class snek:
    def __init__(self) -> None:
        self.head=[r.randint(5,15),r.randint(5,15)]
        self.body=[[0,0],[0,0],[0,0]]
        self.dir=[0,0]
        self.ded=False
        self.start=False
    def move(self):
        
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if self.ded==False:
                        if event.key == pygame.K_LEFT:
                            self.dir=[-1,0]
                        if event.key == pygame.K_RIGHT:
                            self.dir=[1,0]
                        if event.key == pygame.K_DOWN:
                            self.dir=[0,1]
                        if event.key == pygame.K_UP:
                            self.dir=[0,-1]
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()  
        
     
        if self.ded==False:
            self.move2()
            self.head=[self.head[0]+self.dir[0],self.head[1]+self.dir[1]]
            if self.dir!=[0,0]:
                print(self.dir)
                self.start=True
    def move2(self):
        for i in range(len(self.body)):
            i=len(self.body)-1-i
            self.body[i]=self.body[i-1]
        try:
            self.body[0]=self.head
        except:
            pass
    def dead(self):
        if self.start==True:
            for i in self.body:
                if i==self.head:
                    self.ded=True
                    self.dir=[0,0]
                
s=snek()
a=apple()
def draw():
    
    pygame.draw.rect(DIS,red,((a.pos[0]*30)+100,(a.pos[1]*30)+100,30,30))
    if s.ded ==False:
        pygame.draw.rect(DIS,green,((s.head[0]*30)+100,(s.head[1]*30)+100,30,30))
        for i in s.body:
            pygame.draw.rect(DIS,green,((i[0]*30)+100,(i[1]*30)+100,30,30))
    else:
        pygame.draw.rect(DIS,red,((s.head[0]*30)+100,(s.head[1]*30)+100,30,30))
        for i in s.body:
            pygame.draw.rect(DIS,red,((i[0]*30)+100,(i[1]*30)+100,30,30))
while True:
    DIS.fill(BLACK) 
    draw()
    if s.head==a.pos:
        s.body.append(a.pos)
        a=apple()
    s.move()
    s.dead()

    pygame.display.update()
    FramePerSec.tick(FPS)
