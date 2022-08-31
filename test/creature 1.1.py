#new way of rotating polygons. this way is much smoother than using pythagoras and easier to implement
#i dont think that we need to worry about performance too much, becuase i doubt we will use more than 100 points for a creature
#and the program is only noticabley slower when we draw 10,000 points or more, though we arent doing verry much calculations on them 
#but i think that python will be viable for the project.
#a lot of the peices that are needed for the program to function are still unclear
#i do think that this is achievable and within the scope of my skills, also maybe not becuase most of the gaps are due to math and not programing


import math
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
class point:
    def __init__(self,vec,rotation):
        self.p=vec
        self.r=rotation#2*pi/360 should be max
class limb:
    def __init__(self,r,p):
        self.clockwise=False
        self.spin=0
        self.orbit=0
        self.origin=[random.randint(100,900),random.randint(100,900)]
        self.radius=random.randint(50,100)
        self.points=limb.equlpolly(self,self.radius,random.randint(3,7))
        self.hinge=500,100
        self.velocity=0


       # self.points=limb.equlpolly(r,p)
        
        
            
          #  self.points.append(point(i))
    def equlpolly(self,r,p):
        points=[]
        for i in range(p):#64# this part will create the shape
            j=(i)*2*math.pi/p
            x=r*math.cos(j)
            y=r*math.sin(j)
            points.append(point([x+self.origin[0],y+self.origin[1]],j))
        return points

    #def swing(self):
          
        
    def rotate(self):
        test=0

        r=self.radius
        for i in self.points:
            i.r+=.01
            i.p[0]=r*math.cos(i.r)+self.origin[0]
            i.p[1]=r*math.sin(i.r)+self.origin[1]
            #print("hello")
    def dontrotate(self):
        test=0

        r=self.radius
        for i in self.points:
            
            i.p[0]=r*math.cos(i.r)+self.origin[0]
            i.p[1]=r*math.sin(i.r)+self.origin[1]
            #print("hello")

    def orbithinge(self):#now we make it a penguilim
        test=0
        h=self.hinge
        o=self.origin 
        vec=[(o[0]-h[0]),(o[1]-h[1])]
        r=math.sqrt((vec[0])**2+(vec[1])**2)
        #r=self.radius
        a=0.005
        if vec[0]<1:
            a=-a
        self.velocity+=a

        self.orbit+=self.velocity#we can give it velocty by adding and decreasing rotation
        #clockwise rotation when vector OH[0](origin,hinge["x axis"])>0 a(acceloration)=.01 and a=.01 when oh[0]<0
        # a problem will be that we need to take in to acount the radius of OH when we calculate velocity worry about that later though get it working without relative speed first
        self.origin[0]=r*math.cos(self.orbit)+self.hinge[0]
        self.origin[1]=r*math.sin(self.orbit)+self.hinge[1]
        r=0
       # for i in self.points:
        #    i.p[0]=r*math.cos(i.r)+self.origin[0]
         #   i.p[1]=r*math.sin(i.r)+self.origin[1]
    def drawlimb(self):
        for i in range(len(self.points)-1):
            red=(i*1*3,255-i*3,0)
            green=(0,255,255)
           # print(self.points[i].p)
            pygame.draw.circle(DIS,red,(self.points[i].p),5)
            pygame.draw.line(DIS,red,self.points[i].p,self.points[i+1].p)
        print(self.origin)
        pygame.draw.circle(DIS,green,self.origin,5)
        pygame.draw.circle(DIS,red,(self.points[len(self.points)-1].p),5)
        pygame.draw.line(DIS,red,self.points[0].p,self.points[len(self.points)-1].p)
        pygame.draw.circle(DIS,green,self.hinge,5)
        pygame.draw.line(DIS,red,self.origin,self.hinge)
            
            
            
        
class creature:
    def __init__(self,a,b,c):
        self.p=1
            
    
limbs=[]
for i in range(1):
    limbs.append(limb(50,5))




while True:
    DIS.fill(BLACK)
    pygame.font.init() 
    for i in limbs:
        i.orbithinge()


       # i.dontrotate()
        i.rotate()
        i.drawlimb()
        



    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    FramePerSec.tick(FPS)

#     create 2 points that are conected and share pyshics

# things to consider weight # each point will have a weight of 1 # i can see how the pieces fit together but not how they work

# class creature
	

# 	class point# a set of coodernates in space

# 	class bone #2 points with a fixed distance between them

# 	class hinge# fixed point which will not move

# 	class limb# multiple(3+) points conected to make a polygon

# 	class muscle#2 points with a non fixed distance
	