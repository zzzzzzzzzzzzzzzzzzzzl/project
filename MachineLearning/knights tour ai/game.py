from asyncio import events
from string import whitespace
import pygame
import random
from enum import Enum
from collections import namedtuple
import numpy as np
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
white=(255,255,255)

BLOCK_SIZE = 20
SPEED = 10
boardsize=(10,10)


class test:

    def __init__(self, w=boardsize[0], h=boardsize[1]):
        self.w = w*50
        self.h = h*50
        self.board=[]
        self.width=w
        self.height=h
        self.treaded=[]
        for i in range(w):
            self.board.append([])
            for j in range(h):
                self.board[i].append([i,j])

        self.knight=[r.randint(0,self.width-1),r.randint(0,self.height-1)]
       
        self.display = pygame.display.set_mode((self.w, self.h))
        self.clock = pygame.time.Clock()



    def reset(self):
        self.treaded=[]
        self.board=[]
        w=self.width
        h=self.height
        for i in range(w):
            self.board.append([])
            for j in range(h):
                self.board[i].append([i,j])
        self.knight=[r.randint(0,self.width-1),r.randint(0,self.height-1)]




    def play_step(self):

        # 5. update ui and clock
        self._update_ui()
        self.clock.tick(SPEED)
        self.events()
        # 6. return game over and score
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



        pygame.draw.rect(self.display, BLACK, pygame.Rect(self.knight[0]*50+10,self.knight[1]*50+10,30,30))
        pygame.draw.rect(self.display, white, pygame.Rect(self.knight[0]*50+14,self.knight[1]*50+14,22,22))


        pygame.display.flip()

    def validmove(self,move):
        
        m=[[2,1],[-2,1],[2,-1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]]
        valid=[]
        for i in m:
            tba=0
            idea=[self.knight[0]+i[0],self.knight[1]+i[1]]
            if -1<idea[0]<self.width :
                if -1<idea[1]<self.width :
                    if idea not in self.treaded:
                        tba=1
            valid.append(tba)
        valid=[valid,self.knight]
        move=m[move]

        idea=[self.knight[0]+move[0],self.knight[1]+move[1]]


        if -1<idea[0]<self.width :
            if -1<idea[1]<self.width :
                if idea not in self.treaded:
                    self.treaded.append(self.knight)
                    self.knight=idea
                    self.treaded.append(self.knight)
                    self.knight=idea
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
                        if -1<idea[1]<self.width :
                            if idea not in self.treaded:
                                tba=1
                    valid.append(tba)
                  connections.append([valid,j])
        return connections

                #print(valid)
                #move=m[move]
                  #  connections.append(valid)






game = test()
connections=game.getconnections()
print(len(connections))
for i in connections:
    print(i)
# if __name__ == '__main__':


#     while True:         

#         print(game.knight)
#         game.play_step()
#         game.validmove(r.randint(0,7))

