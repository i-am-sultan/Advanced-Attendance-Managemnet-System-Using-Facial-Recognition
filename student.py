from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from PIL.Image import Resampling
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Details Page")



        #======== creating variables  ==========
        self.var_campus=StringVar()
        self.var_department=StringVar()
        self.var_admission_year=StringVar()
        self.var_semester=StringVar()
        self.var_studentID=StringVar()
        self.var_student_name=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_phone_no=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_radio1=StringVar()

        title_lbl=Label(self.root, text="Student Management System",font=("Sans Serif",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=80)

        b2=Button(title_lbl,text="Home", cursor="hand2",command=self.root.destroy,font=("Sans Serif",15,"bold"),bg="green",fg="White")
        b2.place(x=10,y=20,width=100,height=40)

        main_frame=Frame(self.root, bd=2)
        main_frame.place(x=0,y=100,width=1530,height=790)



        #left label frame
        # left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("Sans Serif",20,"bold"),bg="white",fg="black")
        left_frame=LabelFrame(main_frame,bd=2)
        left_frame.place(x=10,y=10,width=700,height=660)

        #current course frame under left label frame
        left_sub_frame = LabelFrame(left_frame, bd=2, text="Current Course Information of the Student",font=("Sans Serif", 18, "bold"), bg="white", fg="black")
        left_sub_frame.place(x=12, y=12, width=680, height=120)

        #Campus
        dep_label=Label(left_sub_frame,text="Campus",font=("Sans Serif", 12, "bold"), bg="white", fg="black")
        dep_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        dep_combo=ttk.Combobox(left_sub_frame,textvariable=self.var_campus,font=("Sans Serif", 10, "bold"),state="readonly",width=18)
        dep_combo['values']=("Select Campus","Rajabajar","AKCSIT","College Street","Kalyani")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=2,sticky=W)

        #department
        dep_label=Label(left_sub_frame,text="Department",font=("Sans Serif", 12, "bold"), bg="white", fg="black")
        dep_label.grid(row=0,column=2,padx=35,pady=5,sticky=W)

        dep_combo=ttk.Combobox(left_sub_frame,textvariable=self.var_department,font=("Sans Serif", 10, "bold"),state="readonly",width=18)
        dep_combo['values']=("Select Department","MCA","MTECH","BTECH")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=2,pady=2,sticky=W)

        #year
        dep_label=Label(left_sub_frame,text="Year of Admission",font=("Sans Serif", 12, "bold"), bg="white", fg="black")
        dep_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        dep_combo=ttk.Combobox(left_sub_frame,textvariable=self.var_admission_year,font=("Sans Serif", 10, "bold"),state="readonly",width=18)
        dep_combo['values']=("Select Year","2020","2021","2022","2023")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,padx=2,pady=2,sticky=W)

        #semester
        dep_label=Label(left_sub_frame,text="Semester",font=("Sans Serif", 12, "bold"), bg="white", fg="black")
        dep_label.grid(row=1,column=2,padx=35,pady=5,sticky=W)

        dep_combo=ttk.Combobox(left_sub_frame,textvariable=self.var_semester,font=("Sans Serif", 10, "bold"),state="readonly",width=18)
        dep_combo['values']=("Select Semester","1st","2nd","3rd","4th","5th","6th")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=3,padx=2,pady=2,sticky=W)

        #Class Student Information under left label frame
        class_student_frame = LabelFrame(left_frame, bd=2, text="Personal Information",font=("Sans Serif", 18, "bold"), bg="white", fg="black")
        class_student_frame.place(x=12, y=150, width=680, height=400)

        #Student ID
        student_id=Label(class_student_frame,text="Student ID",font=("Sans Serif", 12, "bold"), bg="white", fg="black")
        student_id.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_studentID,font=("Sans Serif", 10, "bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        #Student Name
        student_name=Label(class_student_frame,text="Name",font=("Sans Serif", 12, "bold"), bg="white", fg="black")
        student_name.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        student_name_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_student_name,font=("Sans Serif", 10, "bold"))
        student_name_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        #Student Roll
        student_roll=Label(class_student_frame,text="Roll",font=("Sans Serif", 12, "bold"), bg="white", fg="black")
        student_roll.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        student_roll_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_roll,font=("Sans Serif", 10, "bold"))
        student_roll_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        #Student Gender
        student_gender=Label(class_student_frame,text="Gender",font=("Sans Serif", 12, "bold"), bg="white", fg="black")
        student_gender.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        student_gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("Sans Serif", 10, "bold"),state="readonly",width=17)
        student_gender_combo['values']=("Select Gender","Male","Female","Others")
        student_gender_combo.current(0)
        student_gender_combo.grid(row=3, column=1, padx=2, pady=2, sticky=W)


        #Student DOB
        student_dob=Label(class_student_frame,text="DOB",font=("Sans Serif", 12, "bold"), bg="white", fg="black")
        student_dob.grid(row=4,column=0,padx=5,pady=5,sticky=W)

        student_dob_entry = ttk.Entry(class_student_frame, width=20,textvariable=self.var_dob,font=("Sans Serif", 10, "bold"))
        student_dob_entry.grid(row=4, column=1, padx=10, pady=10, sticky=W)


        #Student Phone Number
        student_phnno=Label(class_student_frame,text="Phone No",font=("Sans Serif", 12, "bold"), bg="white", fg="black")
        student_phnno.grid(row=5,column=0,padx=5,pady=5,sticky=W)

        student_phone_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_phone_no,font=("Sans Serif", 10, "bold"))
        student_phone_entry.grid(row=5,column=1,padx=10,pady=10,sticky=W)

        #Student Email
        student_email=Label(class_student_frame,text="Email",font=("Sans Serif", 12, "bold"), bg="white", fg="black")
        student_email.grid(row=6,column=0,padx=5,pady=5,sticky=W)

        student_email_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_email,font=("Sans Serif", 10, "bold"))
        student_email_entry.grid(row=6,column=1,padx=10,pady=10,sticky=W)

        #Student Address
        student_address=Label(class_student_frame,text="Address",font=("Sans Serif", 12, "bold"), bg="white", fg="black")
        student_address.grid(row=7,column=0,padx=5,pady=5,sticky=W)

        student_address_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_address,font=("Sans Serif", 10, "bold"))
        student_address_entry.grid(row=7,column=1,padx=10,pady=10,sticky=W)


        #Radio buttons
        self.var_radio1=StringVar()

        #Button Frame
        button_frame=Frame(left_frame)
        button_frame.place(x=12,y=580,width=680,height=70)

        #save button
        save_btn=Button(button_frame,text="Save",command=self.add_data,font=("Sans Serif", 11, "bold"), bg="blue", fg="white",width=13)
        save_btn.grid(row=0,column=0,padx=2,pady=2)

        #update button
        save_btn=Button(button_frame,text="Update",command=self.update_data,font=("Sans Serif", 11, "bold"), bg="blue", fg="white",width=13)
        save_btn.grid(row=0,column=1,padx=2,pady=2)

        #delete button
        save_btn=Button(button_frame,text="Delete",command=self.delete_data,font=("Sans Serif", 11, "bold"), bg="blue", fg="white",width=13)
        save_btn.grid(row=0,column=2,padx=2,pady=2)

        #reset button
        save_btn=Button(button_frame,text="Reset",command=self.reset_data,font=("Sans Serif", 11, "bold"), bg="blue", fg="white",width=13)
        save_btn.grid(row=0,column=3,padx=2,pady=2)

        #take a photo button
        take_photo_btn = Button(button_frame,command=self.generate_dataset, text="Take a Photo",font=("Sans Serif", 11, "bold"), bg="blue",fg="white", width=13)
        take_photo_btn.grid(row=0, column=4, padx=2, pady=2)

        # #update photo
        # update_btn = Button(button_frame, text="Update Photo",font=("Sans Serif", 11, "bold"), bg="blue",fg="white", width=13)
        # update_btn.grid(row=1, column=2, padx=2, pady=2)

        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,font=("Sans Serif",20,"bold"),fg="black")
        right_frame.place(x=715,y=10,width=800,height=660)

        #==============Searching System=============

        search_frame = LabelFrame(right_frame, bd=2, relief=RIDGE,text="Search System",font=("Sans Serif", 15, "bold"),bg="white", fg="black")
        search_frame.place(x=12, y=10, width=780, height=80)

        #Search Label
        search_label = Label(search_frame, text="Search By",font=("Sans Serif", 12, "bold"), bg="white",fg="black")
        search_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        #Search Combo
        search_combo = ttk.Combobox(search_frame,font=("Sans Serif", 12, "bold"),state="readonly", width=18)
        search_combo['values'] = ("Select","Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=2, sticky=W)

        #Search entry field
        search_entry = ttk.Entry(search_frame, width=13,font=("Sans Serif", 15, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        #Search button
        search_btn = Button(search_frame, text="Search",font=("Sans Serif", 11, "bold"), bg="blue",fg="white", width=13)
        search_btn.grid(row=0, column=3, padx=2, pady=2)

        #Show all button
        showall_btn = Button(search_frame, text="Show All",font=("Sans Serif", 11, "bold"), bg="blue",fg="white", width=13)
        showall_btn.grid(row=0, column=4, padx=2, pady=2)

        #Table frame
        table_frame = LabelFrame(right_frame, bd=2, relief=RIDGE,font=("Sans Serif", 15, "bold"),bg="white", fg="black")
        table_frame.place(x=12, y=120, width=780, height=280)
        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("Campus","Department","Year of Admission","Semester","Student ID","Student Name","Roll","Gender","DOB","Phone","Email","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set) #dummy coloum names
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Campus",text="Campus")
        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Year of Admission",text="Year of Admission")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("Student ID",text="Student ID")
        self.student_table.heading("Student Name",text="Student Name")
        self.student_table.heading("Roll",text="Roll")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Phone",text="Phone")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Address",text="Address")
        self.student_table["show"]="headings"

        self.student_table.column("Campus",width=100)
        self.student_table.column("Department",width=100)
        self.student_table.column("Year of Admission",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("Student ID",width=100)
        self.student_table.column("Student Name",width=100)
        self.student_table.column("Roll",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Phone",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Address",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #============   Adding Student Details function ================
    def add_data(self):
        if self.var_department.get()=="Select Department" or self.var_campus.get()=="Select Campus" or self.var_admission_year.get()=="Select Year" or self.var_semester.get()=="Select Semester":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="sultan",database="face_recognition_attendance")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_campus.get(),
                    self.var_department.get(),
                    self.var_admission_year.get(),
                    self.var_semester.get(),
                    self.var_studentID.get(),
                    self.var_student_name.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_phone_no.get(),
                    self.var_email.get(),
                    self.var_address.get(), 
                    self.var_radio1.get() 
                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been successfully saved",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)


    #==================fetching data from table==========================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root",password="sultan",database="face_recognition_attendance")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert('',END,values=i)
            conn.commit()
        conn.close()

    #=============get cursor==============================
    #today i have watched till: 34:00 minutes 11/08/22
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_campus.set(data[0]),
        self.var_department.set(data[1]),
        self.var_admission_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_studentID.set(data[4]),
        self.var_student_name.set(data[5]),
        self.var_roll.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_phone_no.set(data[9]),
        self.var_email.set(data[10])
        self.var_address.set(data[11])
        self.var_radio1.set(data[12])

    #==============update button function=============
    def update_data(self):
        if self.var_department.get() == "Select Department" or self.var_campus.get() == "Select Campus" or self.var_admission_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.var_studentID.get() == "":
            messagebox.showerror("Error", "All fields are required",
                                 parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host="localhost", username="root",password="sultan",database="face_recognition_attendance")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set campus=%s,department=%s,admission_year=%s,semester=%s,student_name=%s,roll=%s,gender=%s,dob=%s,phone_no=%s,email=%s,address=%s,photo_sample=%s where student_id=%s",
                    (self.var_campus.get(),
                    self.var_department.get(),
                    self.var_admission_year.get(),
                    self.var_semester.get(),
                    self.var_student_name.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_phone_no.get(),
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_radio1.get(),
                    self.var_studentID.get()
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details updated successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)

    #==============delete button function=============
    def delete_data(self):
        if self.var_studentID.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
        else:
            try:
                Delete=messagebox.askyesno("Delete page ",f"Do you want to delete the student {str(self.var_student_name.get())}",parent=self.root)
                if Delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root",password="sultan",database="face_recognition_attendance")
                    my_cursor = conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.var_studentID.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)

    #==============reset button function=============
    def reset_data(self):
        self.var_campus.set("Select Campus")
        self.var_department.set("Select Department")
        self.var_admission_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_studentID.set("")
        self.var_student_name.set("")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_phone_no.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_radio1.set("")

    #====== till now 3rd lecture is completely watched =======
    def generate_dataset(self):
        if self.var_studentID.get()=="":
            messagebox.showerror("Error","To generate dataset. Student ID must be required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="sultan",database="face_recognition_attendance")

                my_cursor=conn.cursor()
                   #user id
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                # for x in myresult:
                #     id+=1
                id=self.var_studentID.get()
                my_cursor.execute("update student set campus=%s,department=%s,admission_year=%s,semester=%s,student_name=%s,roll=%s,gender=%s,dob=%s,phone_no=%s,email=%s,address=%s,photo_sample=%s where student_id=%s",
                (self.var_campus.get(),
                self.var_department.get(),
                self.var_admission_year.get(),
                self.var_semester.get(),
                self.var_student_name.get(),
                self.var_roll.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_phone_no.get(),
                self.var_email.get(),
                self.var_address.get(),
                self.var_radio1.get(),
                self.var_studentID.get()
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #=====load predefined data on face frontal =====
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor=1.3
                    # minimum neighbor=5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while(True): #this should always be "True" not "true" this silly mistake took almost 1 hour. :( 
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(150,150))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==1000:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Dataset generated")
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)
                
    #===========open image function================

'''
Errors that took me more then 1 hour to solve:
1. true != True
2. cv2 is not defined not always mean opencv is not installed properly, it may occur when there is Syntactical Error
3. datatype should match with the value
'''
if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
