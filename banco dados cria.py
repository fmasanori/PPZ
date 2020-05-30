import sqlite3

con = sqlite3.connect('alunos.bd') 
cur = con.cursor()
cur.execute('''create table alunos(login varchar(8),
               ra integer)''')

cur.close()
con.close()
