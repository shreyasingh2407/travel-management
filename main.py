#*********************ADDING FUNCTONS***********************************************************
def addmember():
    def submitadd():
        name=nameval.get()
        age=ageval.get()
        gender=genderval.get()
        contact=contactval.get()
        email=emailval.get()
        membership=membershipval.get()
        id1=idval.get()

        try:
            strr='insert into member1 values(%s,%s,%s,%s,%s,%s,%s);'
            mycursor.execute(strr,(name,age,gender,contact,email,membership,id1))
            con.commit()
            res = messagebox.askyesnocancel('NOTIFICATION','MEMBER ADDED SUCESSFULLY!....Do you want to clean the form?',parent=addroot)
            if(res==True):
                nameval.set('')
                ageval.set('')
                genderval.set('')
                contactval.set('')
                emailval.set('')
                membershipval.set('')
                idval.set('')
        except:
            messagebox.showerror('NOTIFICATION','ID ALREADY EXISTS TRY ANOTHER ID',parent=addroot)
    strr='select * from member1'
    mycursor.execute(strr)
    datas=mycursor.fetchall()
    membertable.delete(*membertable.get_members())
    for i in datas:
        vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
        membertable.insert('',END,values=vv)
            
    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title('NEW MEMBERSHIP!!')
    addroot.config(bg='black')
    addroot.resizable(False,False)
    #--------------------ADD LABEL------------------------------------
    namelabel=Label(addroot,text="Enter Name:",bg='white',font=('times',15,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
    namelabel.place(x=10,y=10)
    agelabel=Label(addroot,text="Enter Age:",bg='white',font=('times',15,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
    agelabel.place(x=10,y=70)
    genderlabel=Label(addroot,text="Enter Gender:",bg='white',font=('times',15,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
    genderlabel.place(x=10,y=130)
    contactlabel=Label(addroot,text="Enter Contact_No:",bg='white',font=('times',15,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
    contactlabel.place(x=10,y=190)
    emaillabel=Label(addroot,text="Enter Email_id:",bg='white',font=('times',15,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
    emaillabel.place(x=10,y=250)
    membershiplabel=Label(addroot,text="Enter Membership:",bg='white',font=('times',15,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
    membershiplabel.place(x=10,y=310)
    member_idlabel=Label(addroot,text="Your Member_id:",bg='white',font=('times',15,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
    member_idlabel.place(x=10,y=370)
    #--------------------------ENTRY BOX---------------------------------------------
    nameval=StringVar()
    ageval=StringVar()
    genderval=StringVar()
    contactval=StringVar()
    emailval=StringVar()
    membershipval=StringVar()
    idval=StringVar()
    
    nameentry= Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=10)
    ageentry= Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=ageval)
    ageentry.place(x=250,y=70)
    genderentry= Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=130)
    contactentry= Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=contactval)
    contactentry.place(x=250,y=190)
    emailentry= Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=250)
    membershipentry= Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=membershipval)
    membershipentry.place(x=250,y=310)
    identry= Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=370)
    #-------------------------ADD BUTTON---------------------------------------------------------
    submitbutton= Button(addroot,text='SUBMIT',font=('roman',15,'bold'),bd=5,width=20,activebackground='red',activeforeground='white',command=submitadd)
    submitbutton.place(x=150,y=430)
    addroot.mainloop()
#*******************************************UPGRADE************************************************************************************************************************    
def upgrademember():
    def update():
        name=nameval.get()
        age=ageval.get()
        gender=genderval.get()
        contact=contactval.get()
        email=emailval.get()
        membership=membershipval.get()
        id1=idval.get()
        if(id1!=''):
            strr='update member1 set name=%s,age=%s,gender=%s,contactno=%s,emailid=%s,membership=%s where memberid=%s'
            
            mycursor.execute(strr,(name,age,gender,contact,email,membership,id1))
            con.commit()
            res=messagebox.showinfo('NOTIFICATION','ID UPDATED SUCESSFULLY',parent=upgraderoot)
            if(res==True):
                nameval.set('')
                ageval.set('')
                genderval.set('')
                contactval.set('')
                emailval.set('')
                membershipval.set('')
                idval.set('')
            datas=mycursor.fetchall()
    strr='select * from member1'
    mycursor.execute(strr)
    datas=mycursor.fetchall()
    #membertable.delete(*membertable.get_members())
    for i in datas:
        vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
        membertable.insert('',END,values=vv)
            
            
    upgraderoot = Toplevel(master=DataEntryFrame)
    upgraderoot.grab_set()
    upgraderoot.geometry('540x540+220+200')
    upgraderoot.title('MEMBERSHIP UPGRADATION!')
    upgraderoot.config(bg='black')
    upgraderoot.resizable(False,False)
    #-----------------------UPGRADE LABEL------------------------------------------------------------------------------------------------
    namelabel=Label(upgraderoot,text="Update Name:",bg='white',font=('times',15,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
    namelabel.place(x=10,y=10)
    agelabel=Label(upgraderoot,text="Update Age:",bg='white',font=('times',15,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
    agelabel.place(x=10,y=70)
    genderlabel=Label(upgraderoot,text="Update Gender:",bg='white',font=('times',15,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
    genderlabel.place(x=10,y=130)
    contactlabel=Label(upgraderoot,text="Update Contact_No:",bg='white',font=('times',15,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
    contactlabel.place(x=10,y=190)
    emaillabel=Label(upgraderoot,text="Update Email_id:",bg='white',font=('times',15,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
    emaillabel.place(x=10,y=250)
    membershiplabel=Label(upgraderoot,text="Update Membership:",bg='white',font=('times',15,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
    membershiplabel.place(x=10,y=310)
    member_idlabel=Label(upgraderoot,text="Your Member_id:",bg='white',font=('times',15,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
    member_idlabel.place(x=10,y=370)
    #--------------------------ENTRY BOX---------------------------------------------
    nameval=StringVar()
    ageval=StringVar()
    genderval=StringVar()
    contactval=StringVar()
    emailval=StringVar()
    membershipval=StringVar()
    idval=StringVar()
    
    nameentry= Entry(upgraderoot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=10)
    ageentry= Entry(upgraderoot,font=('roman',15,'bold'),bd=5,textvariable=ageval)
    ageentry.place(x=250,y=70)
    genderentry= Entry(upgraderoot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=130)
    contactentry= Entry(upgraderoot,font=('roman',15,'bold'),bd=5,textvariable=contactval)
    contactentry.place(x=250,y=190)
    emailentry= Entry(upgraderoot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=250)
    membershipentry= Entry(upgraderoot,font=('roman',15,'bold'),bd=5,textvariable=membershipval)
    membershipentry.place(x=250,y=310)
    identry= Entry(upgraderoot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=370)
    #-------------------------UPGRADE BUTTON---------------------------------------------------------
    submitbutton= Button(upgraderoot,text='SUBMIT',font=('roman',15,'bold'),bd=5,width=20,activebackground='red',activeforeground='white',command=update)
    submitbutton.place(x=150,y=430)
    cc=membertable.focus()
    content=membertable.item(cc)
    pp=content['values']
    if (len(pp) !=0):
        nameval.set(pp[0])
        ageval.set(pp[1])
        genderval.set(pp[2])
        contactval.set(pp[3])
        emailval.set(pp[4])
        membershipval.set(pp[5])
        idval.set(pp[6])
        
    upgraderoot.mainloop()
#********************************************CANCELLATION*******************************************************************************************************************   
def cancelmember():
    cc=membertable.focus()
    content=membertable.item(cc)
    pp=content['values'][6]
    print(content)
    strr='delete from member1 where memberid=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('NOTIFICATION','Membership Deleted sucessfully!')
    strr='select * from member1'
    mycursor.execute(strr)
    datas=mycursor.fetchall()
    #membertable.delete(*membertable.get_members())
    for i in datas:
        vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
        membertable.insert('',END,values=vv)
            
 #***************************************************************************************************************************************************************    
def showallmember():
    strr='select * from member1'
    mycursor.execute(strr)
    datas=mycursor.fetchall()
    #membertable.delete(*membertable.get_members())
    for i in datas:
        vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
        membertable.insert('',END,values=vv)
    
    
#***************************************************************************************************************************************************************
def exitmember():
    res=messagebox.askyesnocancel('NOTIFICATION','Do You Want To Exit?')
    if (res==True):
        root.destroy()
    





#*********INTROSLIDES****************************************************************************
def IntroLabelTick():
    global count,text
    if (count>=len(ss)):
        count=-1
        text=''
        SliderLabel.config(text=text)
    else:
        text=text+ss[count]
        SliderLabel.config(text=text)
    count+=1
    SliderLabel.after(200,IntroLabelTick)
#**************CLOCK******************************************************
def tick():
    time_string=time.strftime('%H:%M:%S')
    date_string=time.strftime('%d/%m/%Y')
    Clock.configure(text='Date : '+date_string+"\n"+" Time : "+time_string)
    Clock.after(200,tick)
#***************COLOURS**********************************************************
import random
colors =['dark blue','red','black','brown']
def IntroLabelColorTick():
    fg=random.choice(colors)
    SliderLabel.config(fg=fg)
#*************CONNECTION OF DATABASE**********************************************************************    
def connectdb():
    def submitdb():
        global con,mycursor
        host=hostval.get()
        user=userval.get()
        passwd=passwdval.get()
        try:
            con=pymysql.connect(host=host,user=user,passwd=passwd)
            mycursor=con.cursor()
        except:
            messagebox.showerror('NOTIFICATION','Data Is Incorrect Please Try Again')
            return
        try:
            strr='create database disha'
            mycursor.execute(strr)
            strr='use disha'
            mycursor.execute(strr)
            strr='create table member1(name char(100),age int(30),gender char(100),contactno int(50) ,emailid varchar(150),membership char(100),memberid int(50))'
            mycursor.execute(strr)
            strr='alter table member1 modify column memberid int not null'
            mycursor.execute(strr)
            strr='alter table member1 modify column memberid int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('NOTIFICATION','Database Created And Now You Are Connected!',parent=dbroot)
        except:
            strr='use disha'
            mycursor.execute(strr)
            messagebox.showinfo('NOTIFICATION','You Are Now Connected To A Database!',parent=dbroot)
        dbroot.destroy()    
    dbroot= Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.resizable(False,False)
    dbroot.config(bg='black')

#********************CONNECTION LABELS**************************************************    
    hostLabel= Label(dbroot,text="Enter Admin:",bg='white',font=('chiller',22,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    hostLabel.place(x=10,y=10)
    userLabel= Label(dbroot,text="Enter User:",bg='white',font=('chiller',22,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    userLabel.place(x=10,y=70)
    passwdLabel= Label(dbroot,text="Enter Password:",bg='white',font=('chiller',22,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    passwdLabel.place(x=10,y=130)
#************************CONNECTDB ENTRY*****************************************************************
    hostval=StringVar()
    userval=StringVar()
    passwdval=StringVar()

    hostentry=Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)
   
    userentry=Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=userval)
    userentry.place(x=250,y=70)
    
    passwdentry=Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=passwdval)
    passwdentry.place(x=250,y=130)
#************************CONNECTIONDB BUTTON************************************************************
    submitbutton= Button(dbroot,text='SUBMIT',font=('roman',15,'bold'),bd=5,width=20,activebackground='red',activeforeground='white',command=submitdb)
    submitbutton.place(x=150,y=190)
    dbroot.mainloop()

        
############################IMPORT FUNCTION################################################################################
from tkinter import *
import time
import random
from tkinter import Toplevel,messagebox
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql

###################################################################################################
root=Tk()
root.title('TRAVEL MANAGEMENT SYSTEM')
root.config(bg='black')
root.geometry('1174x700+200+50')
#root.iconbitmap('mana.icon')#(for setting the icon)
root.resizable(False,False)
from cx_Freeze import *
#***************************FRAMES********************************************************
DataEntryFrame=Frame(root,bg='black',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=600)
#****************************DATAENTRY FRAME********************************************************
frontLabel= Label(DataEntryFrame,text='-----------------WELCOME----------------',width=30,font=('arial',22,'italic bold'),bg='black',fg='white',anchor='w')
frontLabel.pack(side=TOP,expand=True)
addbtn =Button(DataEntryFrame,text='1. BE A NEW MEMBER',width=30,font=('chiller',20,'bold'),bd=6,bg='brown',activebackground='black',activeforeground='white',anchor='w',command=addmember)
addbtn.pack(side=TOP,expand=True)
updatebtn =Button(DataEntryFrame,text='2. UPGRADE YOUR MEMBERSHIP',width=30,font=('chiller',20,'bold'),bd=6,bg='brown',activebackground='black',activeforeground='white',anchor='w',command=upgrademember)
updatebtn.pack(side=TOP,expand=True)
delbtn =Button(DataEntryFrame,text='3. CANCEL YOUR MEMBERSHIP',width=30,font=('chiller',20,'bold'),bd=6,bg='brown',activebackground='black',activeforeground='white',anchor='w',command=cancelmember)
delbtn.pack(side=TOP,expand=True)
showallbtn =Button(DataEntryFrame,text='4. SHOW ALL MEMBERS',width=30,font=('chiller',20,'bold'),bd=6,bg='brown',activebackground='black',activeforeground='white',anchor='w',command=showallmember)
showallbtn.pack(side=TOP,expand=True)
exitbtn =Button(DataEntryFrame,text='5. EXIT',width=30,font=('chiller',20,'bold'),bd=6,bg='brown',activebackground='black',activeforeground='white',anchor='w',command=exitmember)
exitbtn.pack(side=TOP,expand=True)
  





#******************************SHOW DATA FRAME***********************************************
ShowDataFrame=Frame(root,bg='black',relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=550,y=80,width=620,height=600)
#------------------------------------------------------
style=ttk.Style()
style.configure('Treeveiw.Heading',font=('chiller',100,'bold'),foreground='white',bg='black')
style.configure('Treeveiw',font=('chiller',100,'bold'),foreground='white',bg='black')
scroll_x= Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y= Scrollbar(ShowDataFrame,orient=VERTICAL)
membertable= Treeview(ShowDataFrame,columns=('NAME','AGE','GENDER','CONTACT_NO','EMAIL_ID','MEMBERSHIP','ID'),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=membertable.xview)
scroll_y.config(command=membertable.yview)
membertable.heading('NAME',text='NAME')
membertable.heading('AGE',text='AGE')
membertable.heading('GENDER',text='GENDER')
membertable.heading('CONTACT_NO',text='CONTACT_NO')
membertable.heading('EMAIL_ID',text='EMAIL_ID')
membertable.heading('MEMBERSHIP',text='MEMBERSHIP')
membertable.heading('ID',text='MEMBER_ID')
membertable['show']='headings'
membertable.column('ID',width=100)
membertable.column('MEMBERSHIP',width=200)
membertable.column('EMAIL_ID',width=250)
membertable.column('CONTACT_NO',width=200)
membertable.column('GENDER',width=100)
membertable.column('AGE',width=100)
membertable.column('NAME',width=100)

membertable.pack(fill=BOTH,expand=1)



#*************************SLIDER***********************************************************
ss='TRAVEL MANAGEMENT SYSTEM'
count=0
text=''
SliderLabel=Label(root,text=ss,relief=RIDGE,borderwidth=4,font=('chiller',30,'italic bold'),width=35,bg='gold2')
SliderLabel.place(x=260,y=0)
IntroLabelTick()
IntroLabelColorTick()
#************************CLOCK*************************************************************
Clock =Label(root,relief=RIDGE,borderwidth=4,font=('times',14,'bold'),width=20,bg='gold2')
Clock.place(x=0,y=0)
tick()
#****************************CONNECT DATABASE**********************************************  
connectbutton =Button(root,text='CONNECT TO DATABASE',width=23,relief=RIDGE,borderwidth=4,font=('chiller',18,'italic bold'),bg='gold2',activebackground='red',activeforeground='white',command=connectdb)
connectbutton.place(x=930,y=0)
root.mainloop()
#####################################################################################################################################################################
                                                                #*******THE END****#
#####################################################################################################################################################################

    
                 

