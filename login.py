from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from mainprojectdone import super_market


root=Tk()
url=ImageTk.PhotoImage(Image.open("1234.jpg"))
canvas1=Canvas(root,width=2000,height=900)
canvas1.pack(fill="both",expand=True)
canvas1.create_image(0,0,image=url,anchor="nw")
root.title('Login')
root.geometry('2000x900')

     
class sp():
    
    def Login(self):
        username=self.en1.get()
        password=self.en2.get()

        if username=="keerthi" and password=="0198":
            messagebox.showinfo("","login successfully")

            win=Toplevel()
            k=super_market(win)
            win.mainloop()

        elif username=="" and password=="":
            messagebox.showinfo("","Enter the valid details")
        else:
            messagebox.showinfo("","Incorrect username or password")

    def __init__(self, root):
        
            self.lbl1=Label(root,text='User Name',bg='blue',fg='white')
            self.lbl2=Label(root,text='Password',bg='blue',fg='white')
            self.lbl1.place(x=500,y=200)
            self.lbl2.place(x=500,y=250)        
        
            self.en1=Entry()
            self.en2=Entry(show='*')
            self.en1.place(x=600, y=200)
            self.en2.place(x=600, y=250)
       
            self.b1=Button(root, text='Submit',bg='green',fg='white',command=self.Login)
            self.b1.place(x=600, y=300)

root=sp(root)

