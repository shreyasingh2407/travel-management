from tkinter import*
from tkinter import ttk
import random
import datetime
import tkinter.messagebox


class Travel:


    def _init_(self,root):
        self.root = root
        self.root.title("Travel Management System")
        self.root.geometry("1350*750+0+")
        self.root.configure(background='black')


        DateofOrder=StringVar()
        DateofOrder.set(time.strftime("%d/%m/%Y"))
        Receipt_Ref=StringVar()
        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        var5=IntVar()
        var6=IntVar()
        var7=IntVar()
        var8=IntVar()
        var9=IntVar()
        var10=IntVar()
        var11=StringVar()
        var12=StringVar()
        var13=StringVar()


        Firstname=StringVar()
        Surname=StringVar()
        Age=StringVar()
        Gender=StringVar()
        Email_Address=StringVar()
        Membership=StringVar()
        Member_Id=StringVar()



        MainFrame=Frame(self.root)
        MainFrame.grid()


        Tops=Frame(MainFrame ,bd=20 ,width=1350, relief=RIDGE)
        Tops.pack(side=TOP)


        self.lblTitle=Label(Tops, font=('arial',70,'bold'),text="TRAVEL MANAGEMENT SYSTEM")
        self.lblTitle.grid()
        window.mainloop()


#if __name__=='_main_':
    #root=Tk()
    #application=Travel (root)
    #root.mainloop()
