import pygame 
import torch
import numpy as np
import pyautogui
from PIL import Image,ImageDraw
import random as r
from label import label
import time
import os

pygame.init()
window=(1920,1080)
screen = pygame.display.set_mode(window)
clock=pygame.time.Clock()
clock.tick(20)



def update_ui():
    start=time.time()
    arr,path=label.get_arr()  
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            colour=tuple(arr[i][j])  
            pygame.draw.rect(screen,colour,(j*4,i*4,1,1)) 
    end=time.time()
    runtime=end-start 
    print(runtime)
    return path
            


print("about to update")
path=update_ui() 
print(path)
run=True
pos1=0
pos2=0
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_r:
                pos1=0
                pos2=0
                print("SPACE down :reset pos")
                
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_d:
                os.remove(path)
                path=update_ui()
                print("d down")
                
        if event.type== pygame.MOUSEBUTTONDOWN:
            
            if pos1==0:
                pos1=event.pos
                print(pos1)
            elif pos2==0:
                pos2=event.pos
                image=Image.open(path)
                #replace folder
                path_to_red_box_image=path.replace("screenshot","red_box_image")
                path_to_no_red_box_image=path.replace("screenshot","no_box_image")
                #label of coodernates
                path_to_no_red_box_image=path_to_no_red_box_image.replace(".png",str(("here",pos1,pos2))+".png")
                path_to_red_box_image=path_to_red_box_image.replace(".png",str(("here",pos1,pos2))+".png")
                #save image with no red box in folder#only has been labeld
                image.save(path_to_no_red_box_image)
                #draw box around image# not sure if we need this or just the coodernates
                draw=ImageDraw.Draw(image)
                for i in range(5):
                    box_coods=(pos1[0]+i,pos1[1]+i,pos2[0]+i,pos2[1]+i)
                    draw.rectangle(box_coods,outline=(255,0,0))
                #save image, with red box on it
                image.save(path_to_red_box_image)
                pos1=0
                pos2=0
                os.remove(path)
                path=update_ui()
                

    pygame.display.flip()
    
    

    

    
    