from ctypes.wintypes import RGB
from tkinter import *
from tkinter import ttk
from turtle import bgcolor
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from PIL.Image import Resampling


class Developer:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        bg=Image.open("C:\\Users\\offic\\Desktop\\Face Recognition Attendance System\\Images\\developerbg.jpg")
        bg=bg.resize((1530,790),Image.ANTIALIAS)
        self.bgimg=ImageTk.PhotoImage(bg)

        bg_img=Label(self.root,image=self.bgimg)
        bg_img.place(x=0,y=0,width=1530,height=790)

        # title_lbl=Label(bg_img,text="Developer",font=("times new roman",26,"bold"),bg="skyblue",fg="white")
        # title_lbl.place(x=0,y=0,width=1530,height=40)

        # img0=Image.open("C:\\Users\\offic\\Desktop\\Face Recognition Attendance System\\Images\\homelogo.png")
        # img0=img0.resize((63,35),Image.ANTIALIAS)
        # self.photoimg0=ImageTk.PhotoImage(img0)

        # btn1_1=Button(bg_img,image=self.photoimg0,cursor="hand2",command= self.root.destroy,bg="blue")
        # btn1_1.place(x=0,y=0,width=63,height=35)

        # Card Button1 
        img1=Image.open("C:\\Users\\offic\\Desktop\\Face Recognition Attendance System\\Images\\sultan_card.png")
        img1=img1.resize((350,300),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        b1=Button(bg_img,image=self.photoimg1,cursor="hand2",command= self.firoj_details )
        b1.place(x=50,y=80,width=350,height=300)
       
        b1.config(background="#BBFFDB")

        # Card Button2 
        img2=Image.open("C:\\Users\\offic\\Desktop\\Face Recognition Attendance System\\Images\\firoj_card.png")
        img2=img2.resize((350,300),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        b2=Button(bg_img,image=self.photoimg2,cursor="hand2",command= self.firoj_details )
        b2.place(x=410,y=80,width=350,height=300)
       
        b2.config(background="#BBFFDB")

        # Card Button 3
        img3=Image.open("C:\\Users\\offic\\Desktop\\Face Recognition Attendance System\\Images\\jeevan_card.png")
        img3=img3.resize((350,300),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        b3img3=Button(bg_img,image=self.photoimg3,cursor="hand2",command= self.firoj_details )
        b3img3.place(x=770,y=80,width=350,height=300)
       
        b3img3.config(background="#BBFFDB")

        # Card Button4 
        img4=Image.open("C:\\Users\\offic\\Desktop\\Face Recognition Attendance System\\Images\\saikat_card.png")
        img4=img4.resize((350,300),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b4=Button(bg_img,image=self.photoimg4,cursor="hand2",command= self.firoj_details )
        b4.place(x=1130,y=80,width=350,height=300)
       
        b4.config(background="#BBFFDB")

    def firoj_details(self):
        print("Firoj")


if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()