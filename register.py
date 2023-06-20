from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        self.v_fname=StringVar()
        self.v_lname=StringVar()
        self.v_contact=StringVar()
        self.v_email=StringVar()
        self.v_securityQ=StringVar()
        self.v_securityA=StringVar()
        self.v_pass=StringVar()
        self.v_cpass=StringVar()
        self.v_checkb=IntVar()
        self.v_jobtitle=StringVar()
        self.v_gender=StringVar()

        #background image
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\minah_000\Desktop\Login page\Bookshop.jpeg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #left image
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\minah_000\Desktop\Login page\Goodbook.jpg")
        bg_lbl=Label(self.root,image=self.bg1)
        bg_lbl.place(x=50,y=100,width=450,height=550)

        #main frame
        frame=Frame(self.root,bg="black")
        frame.place(x=500,y=100,width=800,height=550)

        register_lbl=Label(frame,text="Registeration",font=("times new roman",20,"bold"),fg="white",bg="black")
        register_lbl.place(x=20,y=20)

        #entry label
        #--ROW 1--
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),fg="white",bg="black")
        fname.place(x=50,y=70)

        self.fname_entry=ttk.Entry(frame,textvariable=self.v_fname,font=("times new roman",15))
        self.fname_entry.place(x=50,y=100,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="white",bg="black")
        l_name.place(x=370,y=70)

        self.txt_lname=ttk.Entry(frame,textvariable=self.v_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=100,width=250)

        #-ROW 2--
        contact=Label(frame,text="Contact",font=("times new roman",15,"bold"),fg="white",bg="black")
        contact.place(x=50,y=130)

        self.txt_contact=ttk.Entry(frame,textvariable=self.v_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=160,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),fg="white",bg="black")
        email.place(x=370,y=130)

        self.txt_email=ttk.Entry(frame,textvariable=self.v_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=160,width=250)

        #__ROW 3__
        security_Q=Label(frame,text="Security Question",font=("times new roman",15,"bold"),bg="black",fg="white")
        security_Q.place(x=50,y=190)
        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.v_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","In what city were you born?","What is the name of your favourite pet?","What high school did you attend?")
        self.combo_security_Q.place(x=50,y=220,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="black",fg="white")
        security_A.place(x=370,y=190)

        self.txt_securityA=ttk.Entry(frame,textvariable=self.v_securityA,font=("times new roman",15))
        self.txt_securityA.place(x=370,y=220,width=250)

        #__ROW 4__
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="black",fg="white")
        pswd.place(x=50,y=250)

        self.txt_pswd=ttk.Entry(frame,show="*",textvariable=self.v_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=280,width=250)

        cpswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="black",fg="white")
        cpswd.place(x=370,y=250)

        self.txt_cpswd=ttk.Entry(frame,show="*",textvariable=self.v_cpass,font=("times new roman",15))
        self.txt_cpswd.place(x=370,y=280,width=250)

        #__ROW 5__
        jobtitle=Label(frame,text="Job Title",font=("times new roman",15,"bold"),bg="black",fg="white")
        jobtitle.place(x=50,y=310)
        
        self.combo_jobtitle=ttk.Combobox(frame,textvariable=self.v_jobtitle,font=("times new roman",15,"bold"),state="readonly")
        self.combo_jobtitle["values"]=("Select","Shopkeeper","Manager")
        self.combo_jobtitle.place(x=50,y=340,width=250)
        self.combo_jobtitle.current(0)

        gender=Label(frame,text="Gender",font=("times new roman",15,"bold"),bg="black",fg="white")
        gender.place(x=370,y=310)
        
        self.combo_gender=ttk.Combobox(frame,textvariable=self.v_gender,font=("times new roman",15,"bold"),state="readonly")
        self.combo_gender["values"]=("Select","Male","Female")
        self.combo_gender.place(x=370,y=340,width=250)
        self.combo_gender.current(0)

        #check button
        checkbtn=Checkbutton(frame,variable=self.v_checkb,text="I agree to the Terms and Conditions and the Privacy Policy.",font=("times new roman",10,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=390)

        #register button
        register_btn=Button(frame,command=self.register_data,text="Sign Up",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="grey",activeforeground="white",activebackground="grey")
        register_btn.place(x=250,y=450,width=200,height=35)

        #login button
        login_btn=Button(frame,text="Already have an account?",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        login_btn.place(x=200,y=490,width=300)

    #register function
    def register_data(self):
        if self.v_fname.get()=="" or self.v_lname.get()=="" or self.v_email.get()=="" or self.v_contact.get()=="" or self.v_securityQ.get()=="Select" or self.v_securityA.get()=="" or self.v_jobtitle.get()=="Select" or self.v_gender.get()=="Select":
            messagebox.showerror("Error","All fields are required.")
        elif self.v_pass.get()!=self.v_cpass.get():
            messagebox.showerror("Error","Password and Confirm Password must be same.")
        elif self.v_checkb.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions to proceed.")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="onedirection",database="sys")
            mycursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.v_email.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another email.")
            else:
                mycursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.v_fname.get(),self.v_lname.get(),self.v_contact.get(),self.v_email.get(),self.v_securityQ.get(),self.v_securityA.get(),self.v_pass.get(),self.v_jobtitle.get(),self.v_gender.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered Successfully")

            
if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()
