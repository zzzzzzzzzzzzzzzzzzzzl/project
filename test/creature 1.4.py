#eeded for the program to function are still unclear
#i do think that this is achievable and within the scope of my skills, also maybe not becuase most of the gaps are due to math and not programing


from cgi import test
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
ground=700
class point:
    def __init__(self,vec,rotation):
        self.p=vec
        self.r=rotation#2*pi/360 should be max
class limb:
    def __init__(self,r,p,hinge=[500,100]):
        self.grounded=False
        self.clockwise=False
        self.spin=0
        self.hinge=hinge
        self.origin=[random.randint(200,400),random.randint(100,400)]
        self.radius=random.randint(50,100)
        self.points=limb.equlpolly(self,self.radius,random.randint(3,8))
        vec=[(self.origin[0]-self.hinge[0]),(self.origin[1]-self.hinge[1])]
        m=math.sqrt((vec[0]**2)+(vec[1]**2)) 
        self.r=m
        self.a= m*0.0001 # this
        self.a2=1
        try:
            t=math.atan(vec[1]/vec[0])
        except:
            t=math.atan((vec[1]+1)/(vec[0]+1))
        if t<0:t+=math.pi
        if vec[1]<0: t+=math.pi#all that stress for 3 lines of code # gets the initial angle of the vector
        self.orbit=t
        #self.a=

        self.dumb=[0,0,0]
        self.velocity=0#velocity is missnamed. this is just rotation per frame to get velocity do pi*radius*(velocity/2pi) note that 2pi is just rotation 
        self.truevelocity=0#
        self.swing=True  

          #  self.points.append(point(i))
    def equlpolly(self,r,p):
        points=[]
        for i in range(p):#64# this part will create the shape
            j=(i)*2*math.pi/p
            x=r*math.cos(j)
            y=r*math.sin(j)
            points.append(point([x+self.origin[0],y+self.origin[1]],j))
        return points
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
                print(self.r,self.origin)
    def arm():
        pass           
    

    def rotate(self):
            test=0

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
    def orbithinge(self):#now we need to make it so that the radius is always constant. when we try to run it as a double pendulum its not constant
        if self.swing==True:
            self.spin+=1
            if self.spin==250:
                self.spin=0
            h=self.hinge
            o=self.origin 
            vec=[(o[0]-h[0]),(o[1]-h[1])]
            rsq=(vec[0])**2+(vec[1])**2
            r=self.r#math.sqrt((vec[0])**2+(vec[1])**2)#radius  
            am=(rsq-(vec[1]**2))/rsq#acceloration multiplier

            a=self.a*am#acceloration
            if vec[0]<1:#clockwise acceloration or counter clockwise acceloration
                a=-a
            self.velocity+=a
            arr=self.dumb#this is a dumb way of decelorating
            arr[0]=arr[1]
            arr[1]=arr[2]
            arr[2]=self.velocity
            if arr[0]<arr[1]>arr[2] or arr[0]>arr[1]<arr[2]:#loss of total velocity 
                self.velocity=self.velocity*.7
                
                
                if self.velocity<(0.0001) and self.velocity>0:
                    self.velocity=0
                   # self.swing=False#if it still has velocity
            self.orbit+=self.velocity
            self.origin[0]=r*math.cos(self.orbit)+self.hinge[0]
            self.origin[1]=r*math.sin(self.orbit)+self.hinge[1]
            v=self.velocity
            pi=math.pi
            self.truevelocity=pi*self.r*(v/(2*pi))#pi*radius*(velocity/2pi)
            print(self.truevelocity)# things we need to do. we need to make this our main velocity this should be what is being kept track of


            
        

        
    def drawlimb(self):
        for i in range(len(self.points)-1):
            red=(self.spin,250-self.spin,self.spin)
            green=(0,80,80)
            pygame.draw.circle(DIS,red,(self.points[i].p),5)
            pygame.draw.line(DIS,red,self.points[i].p,self.points[i+1].p)

        pygame.draw.circle(DIS,green,self.origin,5)
        pygame.draw.circle(DIS,red,(self.points[len(self.points)-1].p),5)
        pygame.draw.line(DIS,red,self.points[0].p,self.points[len(self.points)-1].p)
        pygame.draw.circle(DIS,green,self.hinge,5)
        pygame.draw.line(DIS,red,self.origin,self.hinge)

                  
class creature:
    def __init__(self,l=2):
        self.l=[]
        for i in range(l):
            print(i)
            if i==0:
                 self.l.append(limb(20,3))
            else:
                self.l.append(limb(20,3,self.l[i-1].origin))
            self.l[0].hinge=self.l[len(self.l)-1].origin
    def go(self):
            for i in self.l:
            #    i.orbithinge()
                i.rotate()
                i.gravity()
                i.drawlimb()

#limbs[0].hinge=limbs[2].origin
#centre of gravity
c=creature()




while True:
    DIS.fill(BLACK)
    pygame.font.init() 
    c.go()

    
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
	
