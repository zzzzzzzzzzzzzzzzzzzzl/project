import math
import random

import pygame, sys
from pygame.locals import *

import random as r

pygame.init()
FPS = 30
FramePerSec = pygame.time.Clock()

BLACK = (0, 0, 0)
red=(255,0,0)

DIS = pygame.display.set_mode((1000, 1000))
DIS.fill(BLACK)

pos=[0,200]
class ball:
    def __init__(self,pos,vel):
        self.pos=pos
        self.vel=vel
    def moment(self):
        
        if self.pos[1]>=ground and self.v[0]>1:
            self.v[0]=-self.v[0]+2+int(v*.3)
        self.pos[1]+=self.v[0]
        if pos[1]>=ground+1 and self.v[0]<1:
            self.v[0]=0
            pos[1]=ground
        else:
           v+=1


def redraw():
    global pos
    pygame.draw.circle(DIS,red,(pos),5)
        
def gravity():
    global pos,v,ground,v2,c
    if pos[1]>=ground and v>1:
        v=-v+2+int(v*.3)
    pos[1]+=v
    if pos[1]>=ground+1 and v<1:
        v=0
        pos[1]=ground
        c+=1
        if c==4:
            if v2>0:
                v2-=1
            elif v2<0:
                v2+=1
            c=0
    else:
        v+=1

redraw()
ground=940
v=0
v2=2
c=0
while True:
   # DIS.fill(BLACK)
  #  gravity()
    pygame.display.update()
    pos[0]+=v2
   
    
    

    gravity()
    redraw()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    FramePerSec.tick(FPS)
