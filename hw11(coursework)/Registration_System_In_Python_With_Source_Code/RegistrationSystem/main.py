from tkinter import *
from tkinter import messagebox

#-----Functions/Actions
def validation():
    if email.get()!="" and password.get()!="":
        u_checker = userchecker()
        email_checker = email_existance_checker()
        email_format = emailformat_checker()
        if email_format:
            if u_checker:
                messagebox.showinfo("Information","Sucessfully Login")            
            else:
                if email_checker:
                    messagebox.showerror("Error","Ur Password Is incorrect")
                else:
                    messagebox.showerror("Error",'Ur Email Doesnot Exist , Please Move To SignUp')
        else:
            messagebox.showerror("Error","Email Format Is Invalid")
    else:
        messagebox.showerror("Error","Fill All The Required Feilds")
def emailformat_checker():
    temp = email.get()
    count=-1
    for i in temp:
        count+=1
        if i=="@":
            if temp[count:len(temp)]=="@gmail.com":
                return True
            else:
                return False
    else:
        return False

def userchecker():
    with open("insertion.txt") as rd:
        data = rd.readline()
        while data!="":
            temp = data.split(",")
            if temp[1]==email.get() and temp[2]==password.get():
                return True
            data = rd.readline()
        else:
            return False

def email_existance_checker():
    with open("insertion.txt") as rd:
        data = rd.readline()
        while data!="":
            temp = data.split(',')
            if temp[1]==email.get():
                return True
            data = rd.readline()
        else:
            return False
    

def shifting_form():
    screen.destroy()
    import signup

#-----GUI
screen = Tk()

#-----Variables
email=StringVar()
password = StringVar()

#-----Screen GUI
screen.geometry("700x600")
screen.maxsize(width="700",height="600")
screen.minsize(width="700",height="600")
screen.config(bg="yellow2")
screen.title("Registration")

 #Login Title
title = Label(text="LOG IN",font=("Arial",72,"bold"),pady="5",bg="yellow2",fg="deep sky blue").pack(pady="50")

    #login frame
login_frame = Frame(screen,width="380",height="300",bg="deep sky blue")
login_frame.place(x="162",y="150")
    # login frame widgets
#1
email_label = Label(width="15",padx="5",pady="5",text="User Email",bg="deep sky blue",fg="yellow2",font=("Calibri",20,'bold'))
email_label.place(x="165",y="170")
#2
email_entry = Entry(textvariable=email,width="26",selectbackground="deep sky blue",selectforeground="black",font=("Calibri",15,"italic"))
email_entry.place(x="215",y="210")
#3
password_label = Label(width="15",padx="5",pady="5",text="User Password",bg="deep sky blue",fg="yellow2",font=("Calibri",20,'bold'))
password_label.place(x="188",y="240")
#4
password_entry = Entry(textvariable=password,show="*",width="26",selectbackground="deep sky blue",selectforeground="black",font=("Calibri",15,"italic"))
password_entry.place(x="215",y="280")
#5
login_btn = Button(text="Log In",width="23",font=("Arial",14,"italic"),bg="yellow2",fg="deep sky blue",command=validation)
login_btn.place(x="218",y="330")
#6
txt=Label(text="not a member?",font=("Clibri",12,"italic"),bg="deep sky blue",fg="white").place(x="230",y="390")
#7
sgnup_btn = Button(text="Sign up now",width="14",font=("Calibri",10,"bold"),bg="deep sky blue",fg="white",command=shifting_form).place(x="347",y="390")

screen.mainloop()