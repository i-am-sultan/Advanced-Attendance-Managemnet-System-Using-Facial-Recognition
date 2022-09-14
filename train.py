from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from PIL.Image import Resampling
import cv2
import os
import numpy as np
class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Details Page")

        
        title_lbl=Label(self.root,text="Train Dataset",font=("Euclid circular A",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=80)

        #Button: 
        b1=Button(self.root,text="Train Data",command=self.train_classifier,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b1.place(x=730,y=100,width=180,height=60)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)
        ids=np.array(ids)

        #========train the classifier=======
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset successfully trained")

if __name__ =="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop() 