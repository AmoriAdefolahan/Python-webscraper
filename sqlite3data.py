import json 
import sqlite3

connection = sqlite3.connect('db.sqlite')
cursor = connection.cursor()
cursor.execute('Create Table if not exists Student(name Text, roll Interger)')

traffic = json.load(open('json_file.json'))
columns = ['name', 'cursor', 'roll']
for row in traffic:
    keys  = tuple(row[c] for c in columns)
    cursor.execute('ínsert into student values(?,?,?)', keys)
    print(f'{row["name"]}data inserted Sucessfully')

connection. commit() 
connection. close() 