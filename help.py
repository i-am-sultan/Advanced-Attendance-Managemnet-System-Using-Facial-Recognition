from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from PIL.Image import Resampling

# import PSReadLine 

class Help:
   

    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        bg=Image.open("C:\\Users\\offic\\Desktop\\Face Recognition Attendance System\\Images\\face1.jpg")
        bg=bg.resize((1530,790),Image.ANTIALIAS)
        self.bgimg=ImageTk.PhotoImage(bg)
        bg_img=Label(self.root,image=self.bgimg)
        bg_img.place(x=0,y=0,width=1530,height=790)
        #Home Button
        # b8=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.iExit)
        # b8.place(x=1100,y=450,width=150,height=150)


        b1_8=Button(bg_img,text="Home",cursor="hand2",command= self.root.destroy,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_8.place(x=0,y=0,width=100,height=40)
      


        title_lbl=Label(bg_img,text="Help Desk",font=("times new roman",20,"bold"),bg="blue",fg="white")
        title_lbl.place(x=650,y=40,width=200,height=40)



        help_label=Label(bg_img,text="Address",font=("times new roman",16,"bold"),fg="white",bg="blue")
        help_label.place(x=20,y=620) 

        help_label=Label(bg_img,text="Kolkata,West Bengal 700009",font=("times new roman",14,"bold"),fg="white",bg="blue")
        help_label.place(x=20,y=660) 

        help_label=Label(bg_img,text="Email: attendace@gmail.com",font=("times new roman",12,"bold"),fg="white",bg="blue")
        help_label.place(x=20,y=690)

        help_label=Label(bg_img,text="Contact Us: 9593422553",font=("times new roman",12,"bold"),fg="white",bg="blue")
        help_label.place(x=20,y=718) 

        scrollx=ttk.Scrollbar(bg_img,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(bg_img,orient=VERTICAL)

        self.bg_img = ttk.Treeview(bg_img, xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)              #column name using properly and correct
        scrolly.pack(side=RIGHT, fill=Y)               # i have totally one day lost for incorrect column and wrong sql table
        scrollx.config(command=self.bg_img.xview)
        scrolly.config(command=self.bg_img.yview)

    
    def iExitHelp(self):   #main window to exit
            self.root.destroy()

if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()