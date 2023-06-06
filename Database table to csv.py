# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 12:28:39 2023

@author: neera
"""


# code for exporting tables into database using python 
# the output file will be saved in the folder where this python resides
# convert database files into csv format regardless of any server used
#Neerav Desai

import pyodbc
import csv

server = 'your server name'
database = 'your database name'

connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

connection = pyodbc.connect(connection_string)

table_name = 'table name'
sql_query = f'SELECT * FROM {table_name}'

cursor = connection.cursor()
cursor.execute(sql_query)
rows = cursor.fetchall()

output_file = 'output.csv' #name of your output file .csv format
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    column_names = [column[0] for column in cursor.description]
    writer.writerow(column_names)
    for row in rows:
        writer.writerow(row)

csvfile.close()
connection.close()
