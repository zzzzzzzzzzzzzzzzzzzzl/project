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
        self.hinge=500,100
        #how do we get the starting angle of HO orbit should be equall to [x=r*math.cos(j),y=r*math.sin(j)]
        #we just use trig?? ok i see now 
        # starting angle should be equal to 
        #the value of a should be relative to the radius? 
        #
        self.origin=[random.randint(200,800),random.randint(100,800)]
        #self.origin=[100,100]

        self.radius=random.randint(50,100)
        self.points=limb.equlpolly(self,self.radius,random.randint(3,7))
        vec=[(self.origin[0]-self.hinge[0]),(self.origin[1]-self.hinge[1])]
        m=math.sqrt((vec[0]**2)+(vec[1]**2)) 
        self.a= m*0.00005     #m*0.00005=0.0005 for the ratio of radius to acceleration every 100 radius give us 0.005 more acceleration!
       # acceloration is flawed and missspelt
       # we have x velocity and y velocity
       #y velocity should be affected by acceloration but x velocity should not be. meaning that acceloration should not occur in a pendulum when x=0 for a pendulum because this will mean that acceloration should be 
       #equal to (a^2+b^2)=c  acceloration  multiplier=[a^2/c,b^2/c] this will always return between 1 and 0 for x,y the sum of the two will always be 1 this should be equal roughly to the vector of the 
       # vector of the pendulum at any given point#
       #basicly will tell us if we need to apply the force of gravity or not ie: is it accelorating or not 
        try:
            t=math.atan(vec[1]/vec[0])
        except:
            t=math.atan((vec[1]+1)/(vec[0]+1))
        if t<0:t+=math.pi
        if vec[1]<0: t+=math.pi#all that stress for 3 lines of code # gets the initial angle of the vector
        self.orbit=t
        #self.a=

        self.dumb=[0,0,0]
        self.velocity=0
        self.swing=True


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
    def HOpass0x():
        #how to know if youve passed 0x without creating a mess of bools and variables idgkga
        #have a variable that saves the current state of x the previous state of x and the previous previous state of x
        #a=[1,2,1]
        #if a[1]-a[0]
        # 
        #
        pass
    def orbithinge(self):#now we make it a penguilim
        if self.swing==True:
            test=0
            h=self.hinge
            o=self.origin 
            vec=[(o[0]-h[0]),(o[1]-h[1])]
            rsq=(vec[0])**2+(vec[1])**2
            r=math.sqrt((vec[0])**2+(vec[1])**2)
            am=(rsq-(vec[1]**2))/rsq
            #am=1

            #r=self.radius
            #how does loss work?? when we pass HO[0]=0 #why are you applying it to acceloration. it should go on velocioty t.t
            #where should loss go. if i want to decelerate as we pass HO[0]=0 velocity should sloww pah pah pah pah pah pah pah pah pah pah pah pah # if you know the way you will know the way broadly

            a=self.a*am
            loss=0.01
            if vec[0]<1:
                a=-a
                #self.velocity+=a#ok i see the problem now this will check every single frame rather i just want to add loss once when HO[0]=0
                # the dumb way to do it would be to create a bool variable 
                #since we only want it to trigger once we should 
            

            self.velocity+=a

            arr=self.dumb
            #temp=
            arr[0]=arr[1]
            arr[1]=arr[2]
            arr[2]=self.velocity
            if arr[0]<arr[1]>arr[2] or arr[0]>arr[1]<arr[2]:#if this is true trigger velocity loss
                self.velocity=self.velocity*.7
                if self.velocity<(0.0001) and self.velocity>0:
                    self.velocity=0
                    self.swing=False
                print(self.velocity)
            self.orbit+=self.velocity#we can give it velocty by adding and decreasing rotation
            #clockwise rotation when vector OH[0](origin,hinge["x axis"])>0 a(acceloration)=.01 and a=.01 when oh[0]<0
            # a problem will be that we need to take in to acount the radius of OH when we calculate velocity worry about that later though get it working without relative speed first
            #
            self.origin[0]=r*math.cos(self.orbit)+self.hinge[0]
            self.origin[1]=r*math.sin(self.orbit)+self.hinge[1]
            
    def drawlimb(self):
        for i in range(len(self.points)-1):
            red=(i*1*3,255-i*3,0)
            green=(0,255,255)
            pygame.draw.circle(DIS,red,(self.points[i].p),5)
            pygame.draw.line(DIS,red,self.points[i].p,self.points[i+1].p)

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


        i.dontrotate()
       # i.rotate()
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
	