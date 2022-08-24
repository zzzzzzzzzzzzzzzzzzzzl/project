import math
import random
from turtle import pos

import pygame, sys
from pygame.locals import *

import random as r

pygame.init()
pygame.font.init()
FPS = 60
FramePerSec = pygame.time.Clock()

BLACK = (0, 0, 0)
red=(255,0,0)

ground=800

DIS = pygame.display.set_mode((1000, 1000))
DIS.fill(BLACK)

pos=[r.randint(200,800),r.randint(200,800)]
class ball:
    def __init__(self,p,v):
        self.p=p
        self.v=v
        self.grounded=False
        self.still=False
        self.c=0
        
    
    def draw(self):
        global DIS,red
        pygame.draw.circle(DIS,red,(self.p),5)
    def moment(self):
        if self.still==False:
                x=self.v[0]
                self.p[0]+=self.v[0]
                self.c+=1
                if self.grounded==True:
                    if self.c==10:
                        self.c=0
                        if x>0:
                            self.v[0]-=1
                        if x<0:
                            self.v[0]+=1
                        if x==0:
                            self.still=True
                    
                
            
    def gravity(self):
        global ground
      #  self.p[1]+=1
        if self.grounded==False:
            if self.p[1]>=ground and self.v[1]>1:
                self.v[1]=-(self.v[1]*.5)
            self.p[1]+=self.v[1]
            if self.p[1]>=ground and self.v[1]<2 and self.v[1]>-2:
                self.grounded=True 
            else:
                 self.v[1]+=1  
        else:
            self.p[1]=ground      

def randompos(l,h):
    return [r.randint(l,h),r.randint(l,h)]
balls=[]
for i in range(1):
    v=[r.randint(-3,3),0]
    p=randompos(200,800)
    balls.append(ball(p,v))
text=[]
my_font = pygame.font.SysFont('Comic Sans MS', 30)

my_font = pygame.font.SysFont('Comic Sans MS', 30)
    
    
while True:
    DIS.fill(BLACK)
    pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
    s=str(balls[0].grounded)+str(balls[0].v[0])
    text_surface = my_font.render(s, False, (255, 0, 0))
    DIS.blit(text_surface, (100,100))

    


    for i in balls:
        i.gravity()
        i.moment()
        i.draw()
        


        
   
    

    
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    FramePerSec.tick(FPS)
