from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from train import Train
from recognition import Recognition
from developer import Developer
from help import Help
import os
from tkinter import messagebox
from time import strftime
from datetime import datetime

class Face_Recognition_System:
    
        
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Based Attendance System")

        # def time():
        #     string = strftime('%H:%M:%S %p')#current time for use strftime, %p=pm,am
        #     lbl.config(text = string)
        #     lbl.after(1000, time)

        
        # #image 1
        # img1=Image.open("C:\\Users\\offic\\Desktop\\Face Recognition Attendance System\\Images\\1st.jpg")
        # img1=img1.resize((500,350),Image.Resampling.LANCZOS)
        # self.photoimg1=ImageTk.PhotoImage(img1)

        # f1_label=Label(self.root,image=self.photoimg1)
        # f1_label.place(x=0,y=0,width=400,height=250)

        # #image 2
        # img2=Image.open("C:\\Users\\offic\\Desktop\\Face Recognition Attendance System\\Images\\2nd.jpg")
        # img2=img2.resize((400,250),Image.Resampling.LANCZOS)
        # self.photoimg2=ImageTk.PhotoImage(img2)

        # f2_label=Label(self.root,image=self.photoimg2)
        # f2_label.place(x=580,y=0,width=400,height=250)

        # #image 3
        # img3=Image.open("C:\\Users\\offic\\Desktop\\Face Recognition Attendance System\\Images\\3rd.jpg")
        # img3=img3.resize((400,250),Image.Resampling.LANCZOS)
        # self.photoimg3=ImageTk.PhotoImage(img3)

        # f3_label=Label(self.root,image=self.photoimg3)
        # f3_label.place(x=1150,y=0,width=400,height=250)

        #background image
        bg=Image.open("C:\\Users\\offic\\Desktop\\Face Recognition Attendance System\\Images\\home.png")
        bg=bg.resize((1530,790),Image.Resampling.LANCZOS)
        self.bgimg=ImageTk.PhotoImage(bg)

        bg_label=Label(self.root,image=self.bgimg)
        bg_label.place(x=0,y=0,width=1530,height=790)


        # lbl = Label(bg_label, font = ('Sans Serif',35,'bold'),background="blue", foreground = 'white')
        # lbl.place(x=10,y=10,width=300,height=50)
        # time() 

        #Button: Student Details
        b1=Button(self.root,text="Student Details",command=self.student_details,cursor="hand2",font=("Sans Serif",16,"bold"),bg="#64ad6a",fg="white")
        b1.place(x=280,y=400,width=180,height=50)

        #Button: Detect Face
        b2=Button(self.root,text="Detect Face",command=self.recognize_faces,cursor="hand2",font=("Sans Serif",16,"bold"),bg="#64ad6a",fg="white")
        b2.place(x=510,y=400,width=180,height=50)

        #Button: Check Attendances
        b1=Button(self.root,text="Attendances",cursor="hand2",font=("Sans Serif",16,"bold"),bg="#64ad6a",fg="white")
        b1.place(x=740,y=400,width=180,height=50)

        #Button: Help
        b2=Button(self.root,text="Help",command=self.help,cursor="hand2",font=("Sans Serif",16,"bold"),bg="#64ad6a",fg="white")
        b2.place(x=970,y=400,width=180,height=50)

        #Button: Train the faces
        b1=Button(self.root,text="Train",command=self.train_data,cursor="hand2",font=("Sans Serif",16,"bold"),bg="#64ad6a",fg="white")
        b1.place(x=280,y=480,width=180,height=50)

        #Button: Photos
        b2=Button(self.root,text="Photos",cursor="hand2",command=self.open_img,font=("Sans Serif",16,"bold"),bg="#64ad6a",fg="white")
        b2.place(x=510,y=480,width=180,height=50)

        #Button: Attendance
        b1=Button(self.root,text="Developer",command=self.developers,cursor="hand2",font=("Sans Serif",16,"bold"),bg="#64ad6a",fg="white")
        b1.place(x=740,y=480,width=180,height=50)

        #Button: Exit
        b2=Button(self.root,text="Exit",command=self.exit,cursor="hand2",font=("Sans Serif",16,"bold"),bg="#64ad6a",fg="white")
        b2.place(x=970,y=480,width=180,height=50)

    #=============open faces function=====================
    def open_img(self):
        os.startfile("data")

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def recognize_faces(self):
        self.new_window=Toplevel(self.root)
        self.app=Recognition(self.new_window)
    
    def developers(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

    def exit(self):
        self.check=messagebox.askyesno("Face_Recognition_System","Are Exit this project",parent=self.root)
        if self.check == True:
            self.root.destroy()
        else:
            return


if __name__ == "__main__": #code under this will no longer executable in case of import to another file

    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()