#inserting selected data into a already existing table
import pandas as pd
#from pandas.io import sql
from sqlalchemy import create_engine
import pymysql
#reading from sql table
import mysql.connector as con
mydb=con.connect(host="localhost",user="root",passwd="admin",database="studentdb")
if mydb.is_connected():
    st="select * from details;"
    df1=pd.read_sql(st,mydb)
    print(df1)
    mydb.close()
else:
    print("connection problem")
#changes on the dataframe
    



#writing into file 
    
engine=create_engine('mysql+pymysql://root:admin@localhost/studentdb')
mycon=engine.connect()
df1.to_sql('details',mycon,index=False,if_exists='replace')
