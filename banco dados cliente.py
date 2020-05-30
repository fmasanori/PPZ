import sqlite3

con = sqlite3.connect('alunos.bd') 
cur = con.cursor()

cur.execute('insert into alunos values("masanori", 42)')
cur.execute('insert into alunos values("emengarda", 666)')
cur.execute('select * from alunos')
for x in cur.fetchall():
  print (x)
cur.close()
con.commit()
con.close()
