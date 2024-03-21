import pandas as pd
import pyodbc 
import os
from datetime import datetime
from plyer import notification

# create sql connection
# print(pyodbc.drivers())
connection = pyodbc.connect(driver = "MySQL ODBC 8.3 ANSI Driver",host ='***',database="awesome chocolates",user = 'root',password = '***',trusted_connection = 'yes')
sqlQuery ="select salesperson from people where Team = 'Yummies' and Location = 'Wellington' "

df = pd.read_sql(sql=sqlQuery,con=connection)

df.to_csv(os.environ["userprofile"] + "\\Desktop\\Python_script_2\\" + "SQL_OrderData_" + datetime.now().strftime("%d-%m-%Y,%H%M%S") + ".csv",index=True)

notification.notify(title = "Report Status!!", message = f"Data has been successfully saved .\ \nTotal Rows: {df.shape[0]}\nTotal Columns: {df.shape[1]}",timeout = 10)