###import statements
import sys
import datetime
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog


###function for identifying edges/borders of an image (use the pixel following the last pixel consiting of not white space as the edge )
##edges will stored in an array. Containing the left most and right most column of pixels, top most and bottom most rows of pixels containg non-white space 
def identifyEdges(img):
    edges=[0,0,0,0]
    edgeArray = []
    edgeArray.append(edges)
    n = 0
    x = 0
    while(x < img.shape[1]):
        y=0
        while(y < img.shape[0]):
            pixelColor = img[y,x,2]
            if(pixelColor != 255): 
                if(edges[0] == 0):
                    edges[0]=y
                else:
                    edges[2]=y
                if(edges[1] == 0):
                    edges[1]=x
                else:
                    edges[3]=x
            y += 1
        x += 1
    return edges

def cropToEdges(img, edges):
     cropped_image = img[edges[0]:edges[2], edges[1]:edges[3]]
     return cropped_image



def divideToQuadrant(img):
    quadrant1 = img[0:round(img.shape[0]/2), 0:round(img.shape[1]/2)]
    quadrant2 = img[0:round(img.shape[0]/2), round(img.shape[1]/2):img.shape[1]]
    quadrant3 = img[round(img.shape[0]/2):img.shape[0], 0:round(img.shape[1]/2)]
    quadrant4 = img[round(img.shape[0]/2):img.shape[0], round(img.shape[1]/2):img.shape[1]]
    return [quadrant1,quadrant2,quadrant3,quadrant4]

tk.Tk().withdraw() # part of the import if you are not using other tkinter functions

root = tk.Tk()
root.withdraw()

fn = filedialog.askopenfilenames()
fn = str(fn)
fn = fn[2:(len(fn)-3)]
print(fn)

image = cv2.imread(fn)



#image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)





array = divideToQuadrant(image)

count = 1
for each in array:
# wait untill a any key is pressed to quite the program
    cv2.waitKey(0)
    now = str(datetime.datetime.now())
    
    now = now.replace(':','.')
    


    if(count == 4): 
        print(each[10,10,2])
    edges = identifyEdges(each)
    
    pic = cropToEdges(each, edges)
    
    
    print(now)
    cv2.imwrite(now + str(count) +".jpg", pic)
    count = count + 1

