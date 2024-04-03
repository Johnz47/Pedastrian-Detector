# -*- coding: utf-8 -*-
"""

@author: Johns
"""
# Importing Necessary Libraries
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image,ImageTk
import numpy as np
import os



import imutils
import cv2


# Initializing the GUI
top=tk.Tk()
top.geometry('800x600')
top.title('Pedastrian Detector')
top.configure(background='#CDCDCD')




def play(file_path):
    cap = cv2.VideoCapture(file_path)
    human_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')


    while(True):
    
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        humans = human_cascade.detectMultiScale(gray, 1.9, 1)
        
    
        for (x,y,w,h) in humans:
             cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
             
             

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

def image(file_path):

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    image = cv2.imread(file_path)
  

    (regions, _) = hog.detectMultiScale(image, 
                                    winStride=(4, 4),
                                    padding=(4, 4),
                                    scale=1.05)
  
# Drawing the regions in the Image
    for (x, y, w, h) in regions:
        cv2.rectangle(image, (x, y), 
                  (x + w, y + h), 
                  (0, 0, 255), 2)
 
# Showing the output Image
    cv2.imshow("Image", image)
    cv2.waitKey(0)
  
    cv2.destroyAllWindows()
  


def upload_video():
    try:
        file_path=filedialog.askopenfilename()

     
        play(file_path)
    
    except:
        pass
def upload_image():
    try:
        file_path=filedialog.askopenfilename()

     
        image(file_path)
    
    except:
        pass

upload=Button(top,text="Upload Video",command=upload_video,padx=7,pady=5)
upload.configure(background="#364156",foreground='white',font=('arial',10,'bold'))
upload.pack(side='bottom',pady=50)

upload=Button(top,text="Upload Image",command=upload_image,padx=12,pady=5)
upload.configure(background="#364156",foreground='white',font=('arial',10,'bold'))
upload.pack(side='bottom',pady=50)

heading=Label(top,text="Pedastrian Detector",pady=20,font=('arial',20,"bold"))
heading.configure(background="#CDCDCD",foreground="#364156")
heading.pack()
top.mainloop()