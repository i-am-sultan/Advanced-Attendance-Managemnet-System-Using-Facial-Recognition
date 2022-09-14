from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from PIL.Image import Resampling
import cv2
import os
import numpy as np
import keyboard  # using module keyboard


class Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognizer Page")

        title_lbl6=Label(text="Face Recognition System",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl6.place(x=0,y=0,width=1530,height=80)

        img1=Image.open("C:\\Users\\offic\\Desktop\\Face Recognition Attendance System\\Images\\3rd.jpg")
        img1=img1.resize((1500,750),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f1_label=Label(self.root,image=self.photoimg1)
        f1_label.place(x=0,y=0,width=1530,height=790)
        
        #Button: Student Details
        b1=Button(f1_label,text="Detect Face",command=self.face_recog, cursor="hand2",font=("times new roman",15,"bold"),bg="green",fg="White")
        b1.place(x=690,y=680,width=150,height=50)

        b2=Button(f1_label,text="Home", cursor="hand2",command=self.root.destroy,font=("times new roman",15,"bold"),bg="green",fg="White")
        b2.place(x=10,y=20,width=100,height=50)

#===========Face recognition command=========
    def face_recog(self): #this is the function we are going to call on the button.
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):

            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors) #converting the images into grayscale images

            coord=[] #coordinate for drawing rectangle
            for(x,y,w,h) in features:
                cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w]) #predicting the image with the classifier
                name = ""
                roll = ""
                confidence=int((100*(1-predict/300))) #accuracy checking

                conn=mysql.connector.connect(host="localhost",username="root",password="sultan",database="face_recognition_attendance")
                my_cursor=conn.cursor() #connecting with the database
 
                my_cursor.execute("select student_name from student where student_id="+str(id))
                name=my_cursor.fetchone()
                my_cursor.execute("select roll from student where student_id="+str(id))
                roll=my_cursor.fetchone()
                my_cursor.execute("select department from student where student_id="+str(id))
                department=my_cursor.fetchone()


                # i="+".join(i) 
                # data=my_cursor.fetchall()
                # for i in data:
                #     print(i,end=" ")
                # print()
                # if len(data)>7:
                #     name = data[5]
                #     roll = data[6]
                # print(name,roll)

                if confidence>77:
                    cv2.putText(img,f"Name: {name}",(x,y-95),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
                    cv2.putText(img,f"Roll: {roll}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
                    cv2.putText(img,f"Course: {department}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

                    cv2.putText(img,f"Unknown Face Detected",(x,y-35),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]
            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img, faceCascade, 1.1, 10, (255,2,2), "Face", clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        video_cap=cv2.VideoCapture(1) #0 for laptop camera, other values for other camera
        while True:
            ret,img=video_cap.read()
            img=recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition System",img)

            if cv2.waitKey(1)==13 and 0xFF==ord('q'):
                break
        video_cap.release()
        cv2.destroyAllWindows()   

        
if __name__ =="__main__":
    root=Tk()
    obj=Recognition(root)
    root.mainloop() 