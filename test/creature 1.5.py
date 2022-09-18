#just going to redo some stuff .
#using the "hinge" variable from the last 
import math
from multiprocessing import BoundedSemaphore
import random
import pygame, sys
from pygame.locals import *
import random as r

pygame.init()
pygame.font.init()
BLACK = (0, 0, 0)
red=(255,0,0)
FPS = 30
DIS = pygame.display.set_mode((1000, 1000))
FramePerSec = pygame.time.Clock()
ground=700
def getrot(p):
            add=0
            x,y=p
            for i in [x,y]:
                if i==0:
                 x+=0.001
                 y+=0.001
            if x<0 and y>0:
                add=180
            if x<0 and y<0:
                add=180
            if x>0 and y<0:
                add=360
            j=math.atan(y/x)
            return j
def getpos (r,j):
        return [r*math.cos(j),r*math.sin(j),j]
class point:
    def __init__(self,vec,rotation):
        self.p=vec
        self.r=rotation#2*pi/360 should be max
class limb:
    def __init__(self,r,p,c):
        self.r=0
        self.grounded=False
        self.spin=0
        self.origin=[random.randint(200,400),random.randint(100,400)]
        self.radius=random.randint(50,100)
        #self.points=limb.equlpolly(self,self.radius,random.randint(3,8))
        self.a2=1 
        self.velocity=0
        self.color=(255-(c*100),c*100,c*100)
    def gravity(self):
        if self.grounded==False:
            self.velocity+=self.a2
            self.origin[1]+=self.velocity
            self.colide()
        
    #def swing(self):
    def colide(self):
        #for i in self.points:
            if self.origin[1]>=ground:
                self.origin[1]=ground
                self.velocity=-self.velocity/2
                if -2<self.velocity<2:
                    self.grounded=True
    def arm():
        pass           
    

    def rotate(self):
        test=0

        r=self.radius
        for i in self.points:
            i.r+=.01
            i.p[0]=r*math.cos(i.r)+self.origin[0]
            i.p[1]=r*math.sin(i.r)+self.origin[1]
    def dontrotate(self):
        test=0
        r=self.radius
        for i in self.points:
            i.p[0]=r*math.cos(i.r)+self.origin[0]
            i.p[1]=r*math.sin(i.r)+self.origin[1]
    def drawlimb(self):
        # for i in range(len(self.points)-1):
        #     red=(self.spin,250-self.spin,self.spin)
        #     green=(0,80,80)
        #     pygame.draw.circle(DIS,red,(self.points[i].p),5)
        #     pygame.draw.line(DIS,red,self.points[i].p,self.points[i+1].p)
       # pygame.dra
        green=self.color
        pygame.draw.circle(DIS,green,self.origin,5)
        #pygame.draw.circle(DIS,red,(self.points[len(self.points)-1].p),5)
        #pygame.draw.line(DIS,red,self.points[0].p,self.points[len(self.points)-1].p)

class bone:
    def __init__(self,l1,l2):
        self.l=l1#limb 1
        self.l2=l2#limb2
        self.vec=[self.l.origin[0]-self.l2.origin[0],self.l.origin[1]-self.l2.origin[1]]
        self.m=math.sqrt((self.vec[0]**2)+(self.vec[1]**2)) #magnitude
        self.mid=[(self.l.origin[0]+self.l2.origin[0])/2,(self.l.origin[1]+self.l2.origin[1])/2]
        self.mvec=[self.mid[0]-self.l.origin[0],self.mid[1]-self.l.origin[1]]
        self.mvec2=[-self.mvec[0],-self.mvec[1]]
        self.rot=getrot(self.mvec)
        self.rot2=getrot(self.mvec2)
        print(self.mvec,self.rot,"pale") 
       # print(self.mvec2,self.rot2,"red")
        print("getpos test",getpos(self.m/2,self.rot))
        self.spin=0.1
        
        
         

    def drawbone(self):
        self.velocity=self.l.velocity+self.l.velocity
        self.mid=[(self.l.origin[0]+self.l2.origin[0])/2,(self.l.origin[1]+self.l2.origin[1])/2]
        self.vec=[self.l.origin[0]-self.l2.origin[0],self.l.origin[1]-self.l2.origin[1]]
        pygame.draw.line(DIS,red,self.l.origin,self.mid)
        pygame.draw.line(DIS,red,self.mid,self.l2.origin)
        pygame.draw.circle(DIS,red,self.mid,5)
        d=math.sqrt((self.vec[0]**2)+(self.vec[1]**2)) 
    def rotate(self):
        j=self.spin
        self.rot+=j
        a=getpos(self.m/2,self.rot)
        self.l.origin=[self.mid[0]+a[0],self.mid[1]+a[1]]
    def rotate2(self):
        j=self.spin
        self.rot2+=j
        a=getpos(self.m/2,self.rot2)
        self.l2.origin=[self.mid[0]-a[0],self.mid[1]-a[1]]
    def gravity(self):
        try:
            self.spin=(self.l.velocity-self.l2.velocity)/1000
        except:
            self.spin=0
    #def colision(self):
        
        
# we want velocity to translate into rotation.
# how can we do this??

# we can calc the circumference of the circle or arc of the stick idk what you would call it.
# but we can get circumfernce and we can use this to translate velocity into rotation rotation would only apply when there is a difference in velocity between the 2 points.
# and there should only be a difference in velocity between the two points after the first bounce.

# say p1 velocity=5 and p2 velocity =8 and length=10

# then what should rotation be?

# 10*pi=31.4ish
# dif=5-8 or 8-5 not sure 
# dif=3 or -3
# 31.4*x=3
# x=% of circumfernce
# rotation=9*360

# posotive or negative rotation =

