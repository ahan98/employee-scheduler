#import mysql.connector
import pandas
import sqlalchemy

# init database
#mydb = mysql.connector.connect(
#    host="localhost",
#    user="root",
#    passwd="password",
#    database="employees"
#)

# mycursor = mydb.cursor() # interacts with mysql database

csv = pandas.read_csv("data.csv")
df = pandas.DataFrame(csv)

# import csv table as a table in mysql
database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://root:password@localhost/employees')
df.to_sql(con=database_connection, name='employees', if_exists='replace')

