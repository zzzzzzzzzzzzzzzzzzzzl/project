
import torch
import numpy as np
import pyautogui
from PIL import Image,ImageFilter
import random as r
import matplotlib.pyplot as plt
import os

class label():
    def get_arr(path):
        folder="screenshot"
        content=os.listdir(folder)
        path =os.path.join(path)
        im=Image.open(path)  
        #im=im.filter(ImageFilter.BoxBlur(20))  

        tensor=torch.from_numpy(np.array(im))

        im_array=tensor.numpy()
        arr=im_array.tolist()


        arr2=[]
        for i in range(len(arr)):
            if i%4==0:
                row=[]
                for j in range(len(arr[i])):
                    if j%4==0:
                        row.append(arr[i][j])
                    
                
                arr2.append(row)
        return arr2,path
        # im=Image.fromarray(im_array)


        # print("about to show image")
        # plt.imshow(arr)
        # plt.show()

        # plt.imshow(im_array)
        # plt.show()