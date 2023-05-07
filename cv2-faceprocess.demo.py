###
import cv2
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import time

fps = 25

#
sleeping = fps/10

#
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier("haarcascade_fullbody.xml")
glasses_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

def process(img):
    global face_cascade,body_cascade,glasses_cascade
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #faces
    faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05,  minNeighbors=5)
    for x,y,w,h in faces:  
        img = cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),3)
    #bodys
    bodys = body_cascade.detectMultiScale(gray_img, scaleFactor = 1.01,  minNeighbors=5)
    for x,y,w,h in bodys:
        img = cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,255),3)
    #
    glasss = glasses_cascade.detectMultiScale(gray_img, scaleFactor = 1.2,  minNeighbors=5)
    for x,y,w,h in glasss:
        img = cv2.rectangle(img, (x,y), (x+w,y+h),(255,128,0),3)
        
    img = cv2.flip(img, 1)
    return img,faces,bodys

def cv2PIL(img_cv):
    return Image.fromarray(cv2.cvtColor(img_cv,cv2.COLOR_BGR2RGB))

def PIL2cv(img_pil):
    ar = np.array(img_pil)
    return cv2.cvtColor(ar,cv2.COLOR_RGB2BGR)

cap = cv2.VideoCapture(0)#创建摄像头对象
#界面画布更新图像
def tkImage(frame):
    frame = cv2.flip(frame, 1) #摄像头翻转
    cvimage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    pilImage=Image.fromarray(cvimage)
    pilImage = pilImage.resize((image_width, image_height),Image.LANCZOS)
    tkImage =  ImageTk.PhotoImage(image=pilImage)
    return tkImage

def autoresize(img):
    img = img.resize((image_width, image_height),Image.LANCZOS)
    return img

top = tk.Tk()
top.title('')

image_width = 600
image_height = 500
canvas = Canvas(top,bg = 'white',width = image_width,height = image_height )#绘制画布
canvas.place(x = 150,y = 50)
canvas2 = Canvas(top,bg = 'white',width = image_width,height = image_height )#绘制画布
canvas2.place(x =850 ,y = 50)

def set_fps(newfps):
    global sleeping
    fps = int(newfps)
    sleeping = 10/fps
    print(f'fps set to {fps},sleep is {sleeping}')
'''
scale = tk.Scale(top,
             label='FPS',
             from_=1,
             to= 60,
             orient=tk.HORIZONTAL,
             length=400,
             showvalue=False, 
             command=set_fps).place(x=0,y=0)
'''
def show_process2():
    global isprocess
    isprocess = True


tk.Button(top,text="process",command=show_process2).place(x=300,y=2)

isprocess = False

def loop(a=0):
    while True:
        ref,frame=cap.read()
        pilpic = tkImage(frame)
        cvpic = frame
        canvas.create_image(0,0,anchor = 'nw',image = pilpic)
        
        if isprocess == True:
            isprocess == False
            cvpic = frame
            process2,faces,bodys = process(cvpic)
            process2 = cv2PIL(process2)
            process2 = autoresize(process2)
            process2 = ImageTk.PhotoImage(process2)
            canvas2.create_image(0,0,anchor = 'nw',image = process2)
            print(f"bodys: {bodys}\nfaces:{faces}")
        top.update()
        print("update")
        
import threading

mt = threading.Thread(target=loop)
mt.start()

top.mainloop()