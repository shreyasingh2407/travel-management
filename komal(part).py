#DATABASE CREATION:
import mysql.connector as sql
Conn=sql.connect(host=’localhost’,user=’root’,password=’manage
R’,database=’travel_bookings’)
C1=conn.cursor()
If conn.is_connected:
    C1.execute(“create database travel_booking”)
    Print(“database created successfully”)
TABLE 1 CREATION:
Import mysql.connector as sql
Conn=sql.connect(host=’localhost’,user=’root’,password=’manage
R’,database=’travel_bookings’)
C1=conn.cursor()
C1.execute(‘create table accounts(Phone_number bigint(13)
Primary key,name varchar(30),password  bigint(10));’)
Conn.commit()
TABLE 2 CREATION:
Import mysql.connector as sql
Conn=sql.connect(host=’localhost’,user=’root’,password=’manage
R’,database=’travel_bookings’)
C1=conn.cursor()
C1.execute(‘create table customer_bookings(Phone_number
Bigint(13) ,FOREIGN KEY(Phone_number) REFERENCES
Accounts(Phone_number),Your_location
Varchar(30),Your_destination varchar(30),time
Varchar(30),Driver varchar(60),Urgency
Varchar(30),date_booked varchar(90));’)
Conn.commit()

import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',password='manage
r',database='travel_booking')
c1=conn.cursor()
conn.autocommit==True
from time import gmtime, strftime
n=strftime("%a, %d %b %Y", gmtime())
n=str(n)
today=n[5:]
 print('                 ','____TRAVEL DAILY welcomes
U!!!!!!____')
print()
print('
print()
print('Press 1 to Login')
print('Press 2 Create account')
print("press 3 delete account")
print('Press 4 to Exit')
print()
choice=int (input('Enter your choice='))
if choice ==1:
                print()
',n)
                a=int(input('Enter your phone number='))
                #Name of the person
                u=("select  name from accounts where
phone_number = "+str(a)+";")
                c1.execute(u)
                #Wrong phone number[account doesn't exist]
                datan=c1.fetchall()
                s=c1.rowcount
                s=abs(s)
                if s!= 1:
                    print()
                    print("*********ACCOUNT
DOESN'T EXIST**********")

print()
                    create=int(input("Press 32 to create
account {{or}} Press 0 to exit="))
Number='))
if create==32:
    phone_number=int(input('Phone
    name=str(input('Name='))
    password =str(input( 'password[10]='))
    c1.execute("insert into
accounts(Phone_number,password,name )values(" +
str(phone_number) +",'" +password  + "',' "+name+" ')")
                        conn.commit()
                        print('Account sucessfully Created')
                        import sys
                        sys.exit()
                    else:
                        import sys
sys.exit()
                datan=datan[0]
                datan=list(datan)
                datan= datan[0]
                datan= str(datan)
            #selecting password
y="select password from accounts where
phone_number =({})".format(a)
                c1.execute(y)
                data=c1.fetchall()
                data=data[0]
                data=list(data)
                data=data[0]
                b=int(input('Enter your password='))
                if b!=data:
print()
                    print("*********INVALID
PASSWORD**********")
                conn.commit()
                if b==data:
                    print()
                    print("LOGGED  IN !!!!!")
                    print()
                    print("HI",datan,"!!")
                    print()
                    print("What can I do for you?")
                    print()
                    print('12.Book for a board')
                    print('13.Bill verification')

print('14.My travel log')
                    print('0.Exit')
                    print()
                    choice1=int(input('Enter Your Choice='))
                    if choice1==0:
                        print()
