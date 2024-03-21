import pyodbc
import pandas as pd
import os
from datetime import datetime
from plyer import notification

# create SQL connection
# to find driver name -> print(pyodbc.drivers())
# to find host name MySQL -> select@@hostname
# to find database name MySQL -> show databases

connection = pyodbc.connect(driver = '{MySQL ODBC 8.3 ANSI Driver}',host = '***',database ="walmartsalesdata",user = 'root',password = '***',trusted_connection = 'yes')

# SQL command to read the data
sqlQuery = "select * from sales where city = 'Yangon'"

# Getting the data from sql into pandas dataframe
df = pd.read_sql(sql = sqlQuery, con = connection)

# Export the data to desktop
df.to_csv(os.environ["userprofile"] + "\\Desktop\\Python_Script\\" + "SQL_OrderData_"+ datetime.now().strftime("%d-%b-%Y %H%M%S") + ".csv",index=False)

# Display notification to user
notification.notify(title = "Report Status!!", message = f"Data has been successfully saved .\ \nTotal Rows: {df.shape[0]}\nTotal Columns: {df.shape[1]}",timeout = 10)