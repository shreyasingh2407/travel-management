#TRAVEL MANAGEMENT SYSTEM
import pandas as pd
import mysql.connector as con
import random
from sqlalchemy import create_engine
import pymysql
mydb=con.connect(host='localhost',user='root',passwd='123456',database='SHREYA')
mycursor=mydb.cursor()
if mydb.is_connected():
    st='select* from MEMBERSHIP;'
    v='select* from member;'
    df=pd.read_sql(st,mydb)
    df1=pd.read_sql(v,mydb)
    
    print(df)
    mydb.close()
else:
   print("Connection Problem")
      
g=1050
p=1550
s=900
r=550


d=input("Enter 1. For New Membership, 2. For Upgradation, 3. For Surrender:")
#BOOKING FUNCTION
if d=='1':
    m1=str(input("Enter your name:"))
    m2=input("Enter your age:")
    m3=input("Enter your gender:")
    m4=input("Please enter your contact_no:")
    m5=input("Enter your E-mail address:")
    m6=input("Enter the membership type wanted('g' for gold,'p' for platinum,'s' for silver,'r' for regular):")
    m=random.randint(1000,2000)
    print("YOUR UNIQUE MEMBER ID IS:",m)
    mydb=con.connect(host='localhost',user='root',passwd='123456',database='disha')
    mycursor=mydb.cursor()
    strr='insert into member1 values(%s,%s,%s,%s,%s,%s,%s);'
    mycursor.execute(strr,(m1,m2,m3,m4,m5,m6,m))
    strr1='select * from member1'
    mycursor.execute(strr1)
    datas=mycursor.fetchall()
    #membertable.delete(*membertable.get_members())
    for i in datas:
        vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6]]
        v.append('',END,values=vv)
    
    
    
    mydb.close()
    mycursor.close()
    if m6=='G' or m6=='g':
        q=("YOUR TOTAL DUE IS Rs.1050(including taxes)")
        print(q)
    elif m6=='P' or m6=='p':
        q=("YOUR TOTAL DUE IS Rs.1550(including taxes)")
        print(q)
    elif m6=='S' or m6=='s':
        q=("YOUR TOTAL DUE IS Rs.900(including taxes)")
        print(q)
    elif m6=='R' or m6=='r':
        q=("YOUR TOTAL DUE IS Rs.550(including taxes)")
        print(q)
    else:
        print("MEMBERSHIP TYPE INVALID! PLEASE ENTER IT AGAIN!")
        m6=input("Enter the type of Membership wanted(type G for gold,P for platinum,S for silver,R for regular):")
        
    m7=input("Enter mode of transaction(P FOR PAYTM ,CR FOR CREDIT):")
    if m7=='p' or m7=='P':
        p=input("Enter your PAYTM no.:")
        p1=input('Enter OTP:')
        print("PAYMENT SUCESSFULL!")
    elif m7=='CR' or m7=='cr':
        print("Please enter your card details:\n")
        c1=input("Enter the card number:")
        l=len(c1)
        if l==16:
            c2=input("Enter the expiry date:")
        else:
            print("Please check your card no and enter again")
            c1=int(input("Enter the card number:"))
        c2=int(input("Enter your cvv no:"))
        c3=int(input("Enter the amount payable:"))
        if c3==q:
            c4=input("Enter the OTP:")
        else:
            print("RECHECK THE AMOUNT PAYABLE AND ENTER AGAIN")
            c3=int(input("Enter the amount payable:"))
        m=random.randint(1000,2500)
                          
        
        print("YOUR UNIQUE MEMBER ID IS:",m)
    print("TRANSACTION SUCESSFULL!")
    #APPENDING THE DATA
    data={'NAME':'m1','AGE':'m2','GENDER':'m3','CONTACT_NO':'m4','EMAIL_ID':'m5','MEMBERSHIP':'m6','MEMBER_ID':'m'}
    df1=pd.DataFrame(data,columns =['NAME','AGE','GENDER','CONTACT_NO','EMAIL_ID','MEMBERSHIP','MEMBER_ID'],index=['1','2','3','4','5','6'])
    mydb=con.connect(host='localhost',user='root',passwd='123456',database='disha')
    #engine=create_engine('mysql+pymysql://root:admin@localhost/SHREYA')
    #mycon=engine.connect()
    #engine.raw_connection()
    df1.head(1).to_sql('member1',mycon,index=False,if_exists='append')
    mydb.close()
    print("CONGRATULATIONS! YOU ARE SUCESSFULLY REGISTERED AS A MEMBER.")


#UPGRADATION FUNCTION    
    
elif d=='2': 
    print("-----THE MEMBER DETAILS ARE-----:")
    print(df1)
    #def dupdate():
        #r=input("Enter your name:")
        #pr=input("Enter the type of membership you want to upgrade to(type G for gold,P for platinum,S for silver,R for regular):")
        #st="update member set membership={} where name={}".format(pr,r)
       
        #mycursor.execute(st)
        #mydb.commit()
    u1=input("Enter your name:")
    u2=input("Enter your age:")
    u3=input("Enter your gender:")
    u4=input("Enter your email_id:")
    u5=input("Enter type of membership(wanted):")
    u6=input("Enter your MEMBER ID:")
    print("YOUR PREVIOUS MEMBERSHIP PAYMENT IS REFUNDED!! :).IF YOU DO NOT RECEIVE YOUR PAYMENT WITHIN 24 HRS ,PLEASE CONTACT US AT GOVERNMENTBOOKINGS_HELPDESK@GMAIL.COM WITHIN 72 WORKING HOURS.THANK YOU!")
    u4=input("Enter the type of membership you want to upgrade to(type G for gold,P for platinum,S for silver,R for regular):")
    if u4=='G' or u4=='g':
        print("YOUR TOTAL DUE IS Rs,",g,"(including taxes)")
    
    elif u4=='P' or u4=='p':
        print("YOUR TOTAL DUE IS Rs.",p,"(including taxes)")
        
    elif u4=='S' or u4=='s':
        print("YOUR TOTAL DUE IS Rs.",s,"(including taxes)")
        
    elif u4=='R' or u4=='r':
        print("YOUR TOTAL DUE IS Rs.",r,"(including taxes)")
        
    else:
        print("MEMBERSHIP TYPE INVALID! PLEASE ENTER IT AGAIN!")
        u4=input("Enter the type of Membership you want to upgrade to(type G for gold,P for platinum,S for silver,R for regular):")
            
            
    u5=input("Enter mode of transaction(P FOR PAYTM ,CR FOR CREDIT):")
    if u5=='p' or u5=='P':
        p=input("Enter your PAYTM no.:")
        p1=input('Enter OTP:')
        print("PAYMENT SUCESSFULL!")
        m=random.randint(1000,2000)
        print("YOUR UNIQUE MEMBER ID IS:",m)
    elif u5=='CR' or u5=='cr':
        print("Please enter your card details:\n")
        c1=input("Enter the card number:")
        
        l=len(c1)
        if l==16:
            c2=input("Enter the expiry date:")
        else:
            print("Please check your card no and enter again")
            c1=int(input("Enter the card number:"))
            
        c2=int(input("Enter your cvv no:"))
        c3=int(input("Enter the amount payable:"))
        if c3==u4:
            c4=input("Enter the OTP:")
        else:
            print("RECHECK THE AMOUNT PAYABLE AND ENTER AGAIN")
            c3=int(input("Enter the amount payable:"))
        m=random.randint(1000,2500
                          )
        
        print("YOUR UNIQUE MEMBER ID IS:",m)
        
    print("TRANSACTION SUCESSFULL!")
        
    print("CONGRATULATIONS! YOUR MEMBER DETAILS ARE SUCESSFULLY UPGRADED.")
#CANCELLATION FUNCTION
else:
    print("-----TO DELETE YOUR MEMBERSHIP-----")
    #def ddelete():
        #t=input("Enter your name:")
        #qt="delete from member where name={}".format(t,)
       # mycursor.execute(qt)
       # mydb.commit()
        
        
        
    q1=input("Enter your name:")
    q2=input("Enter your Member-id:")
    q3=input("Enter your membership type:")
#If details matches
    #DROP
    print("YOUR MEMBERSHIP IS CANCELLED!\n")
    print("YOUR PAYMEMNT WILL BE REFUNDED WITHIN 24 WORKING HOURS!")
    print("IF YOU HAVE ANY OTHER ISSUES OR QUERY PLEASE CONTACT US AT GOVERNMENTBOOKINGS_HELPDESK@GMAIL.COM")
    print("THANK YOU! FOR CHOOISNG OUR SERVICES.")

    

    
        
        
        
    
       

