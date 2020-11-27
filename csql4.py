#inserting selected data into a already existing table
import pandas as pd
#from pandas.io import sql
from sqlalchemy import create_engine
import pymysql
raw_data1 = {'name': ['Mihir', 'Mahip'], 'age': [15, 16], 'favorite_color': ['green', 'burgendy'],  'grade': [89, 92.5]}
df1 = pd.DataFrame(raw_data1, columns = ['name', 'age',  'favorite_color', 'grade'])
print(df1)
engine=create_engine('mysql+pymysql://root:admin@localhost/studentdb')
mycon=engine.connect()
df1.tail(1).to_sql('details',mycon,index=False,if_exists='append')
