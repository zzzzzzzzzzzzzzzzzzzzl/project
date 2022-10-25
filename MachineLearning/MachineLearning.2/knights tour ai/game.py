from asyncio import events
from string import whitespace
import pygame
import random
from collections import namedtuple
import random as r

pygame.init()


# rgb colors
WHITE = (255, 255, 255)
RED = (200,0,0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0,0,0)
dark=(181,136,99)
darkdark=(50,50,40)
light=(240,217,181)
lightlight=(100,100,100)
linecolor=(0,0,0)
white=(255,255,255)

BLOCK_SIZE = 20
SPEED = 2000
a=r.randint(8,15)
b=r.randint(8,15)
boardsize=(8,8)


class test:

    def __init__(self, w=boardsize[0], h=boardsize[1]):
        self.max=a*b
        self.w = w*50
        self.h = h*50
        self.board=[]
        self.width=w
        self.height=h
        self.treaded=[]
        self.moves=[]
        for i in range(w):
            self.board.append([])
            for j in range(h):
                self.board[i].append([i,j])

        self.knight=[r.randint(0,self.width-1),r.randint(0,self.height-1)]
        self.moves.append(self.knight)
        self.treaded.append(self.knight)

        self.display = pygame.display.set_mode((self.w, self.h))
        self.clock = pygame.time.Clock()
        self.lowest=0
        self.l=[0,0,0,0,0,0,0,0]
        self.gameover=False
        self.turn=0
        self.adjcon=self.getstate([[2,1],[-2,1],[2,-1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]],0)
        

    def reset(self):
        self.moves=[]
        self.treaded=[]
        self.board=[]
        w=self.width
        h=self.height
        for i in range(w):
            self.board.append([])
            for j in range(h):
                self.board[i].append([i,j])
        self.knight=[r.randint(0,self.width-1),r.randint(0,self.height-1)]
        self.moves.append(self.knight)
        
        
        self.lowest=0
        self.l=[0,0,0,0,0,0,0,0]
        self.gameover=False
        self.turn=0
        self.adjcon=self.getstate([[2,1],[-2,1],[2,-1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]],0)




    def play_step(self,action):
            self.turn+=1
            self.events()

            self._update_ui()
            self.clock.tick(SPEED)
            self.validmove(action)
            if self.gameover==True:
                self.reward=-10
            
            return self.gameover,self.reward,self.turn

        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.reset()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.validmove(r.randint(0,7))

        




    def _update_ui(self):
        self.display.fill(BLACK)

        for i in range(len(self.board)): 
           for k in range(len(self.board[0])):
                if self.board[i][k] not in self.treaded:
                    if i %2==0 and k%2==0:
                        pygame.draw.rect(self.display, dark, pygame.Rect(self.board[i][k][0]*50,self.board[i][k][1]*50,50,50))
                    if i %2==0 and (k+1)%2==0:
                        pygame.draw.rect(self.display, light, pygame.Rect(self.board[i][k][0]*50,self.board[i][k][1]*50,50,50))
                    if (i+1)%2==0 and k%2==0:
                        pygame.draw.rect(self.display, light, pygame.Rect(self.board[i][k][0]*50,self.board[i][k][1]*50,50,50))
                    if (i+1)%2==0 and (k+1)%2==0:
                        pygame.draw.rect(self.display, dark, pygame.Rect(self.board[i][k][0]*50,self.board[i][k][1]*50,50,50))
                else:
                    if i %2==0 and k%2==0:
                        pygame.draw.rect(self.display, darkdark, pygame.Rect(self.board[i][k][0]*50,self.board[i][k][1]*50,50,50))
                    if i %2==0 and (k+1)%2==0:
                        pygame.draw.rect(self.display, lightlight, pygame.Rect(self.board[i][k][0]*50,self.board[i][k][1]*50,50,50))
                    if (i+1)%2==0 and k%2==0:
                        pygame.draw.rect(self.display, lightlight, pygame.Rect(self.board[i][k][0]*50,self.board[i][k][1]*50,50,50))
                    if (i+1)%2==0 and (k+1)%2==0:
                        pygame.draw.rect(self.display, darkdark, pygame.Rect(self.board[i][k][0]*50,self.board[i][k][1]*50,50,50))
        for i in range(len(self.moves)):
            try:
                pygame.draw.line(self.display, BLACK, (self.moves[i][0]*50+25,self.moves[i][1] *50+25), (self.moves[i+1][0]*50+25,self.moves[i+1][1]*50+25), 3)
            except:
                pass


        pygame.draw.rect(self.display, BLACK, pygame.Rect(self.knight[0]*50+10,self.knight[1]*50+10,30,30))
        pygame.draw.rect(self.display, white, pygame.Rect(self.knight[0]*50+14,self.knight[1]*50+14,22,22))


        pygame.display.flip()

    def validmove(self,action):
        if type(action)==list:
            action=action.index(1)
        self.reward=0
        m=[[2,1],[-2,1],[2,-1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]]
        
        move=m[action]
        idea=[self.knight[0]+move[0],self.knight[1]+move[1]]

        self.gameover=True
        if -1<idea[0]<self.width :
            if -1<idea[1]<self.height :
                if idea not in self.treaded:
                    self.treaded.append(self.knight)
                    self.knight=idea
                    self.gameover=False
                    self.moves.append(idea)
        self.getstate(m,action)
        
    

                

     
        
    def getstate(self,m,action):
        c=0
        arr=[]
        adj=[]
        for i in m:
            idea=[self.knight[0]+i[0],self.knight[1]+i[1]]
            iv=False
            if -1<idea[0]<self.width :
                if -1<idea[1]<self.height :
                    if idea not in self.treaded:
                       iv=True
                       c+=1
            if iv==True:
                adj.append(idea)
            else:
                adj.append(True)
                    
        arr.append(c)
        adjcon=[]
        for j in adj:
            c=0
            if j==True:
                c=111
            if j!=True:
                for i in m:
                    idea=[j[0]+i[0],j[1]+i[1]]
                    if -1<idea[0]<self.width :
                        if -1<idea[1]<self.height :
                            if idea not in self.treaded:
                                c+=1
            if c==0:c=111
            
            adjcon.append(c)

        if min(self.l)==self.l[action]:
            self.reward=10
        else:
            self.reward=0
        self.l=adjcon
        self.adjcon=adjcon



                    
        arr.append(c)
        
        return adjcon
    def getstateNEAT(self):
        arr=[]
        

        for i in self.board:
            
            for j in i:
                tba=0
                if j in self.treaded:
                   tba=1
                if j ==self.knight:
                    tba=2
            
                arr.append(tba)
        return arr

    def getconnections(self):
        connections=[]
        for k in self.board:
            for j in k:
                  m=[[2,1],[-2,1],[2,-1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]]
                  valid=[]
                  for i in m:
                    tba=0
                    idea=[j[0]+i[0],j[1]+i[1]]
                    if -1<idea[0]<self.width :
                        if -1<idea[1]<self.height :
                            if idea not in self.treaded:
                                tba=1
                    valid.append(tba)
                  connections.append([valid,j])
        return connections






# game = test()
# game.getstateNEAT()
# if __name__ == '__main__':


#     while True:         

#         print(game.play_step(r.randint(0,7)))
#       #  game.validmove(r.randint(0,7))

