import sqlite3

db = sqlite3.connect('test1.db')
db.execute('drop table if exists tests')
db.row_factory = sqlite3.Row
db.execute('create table tests(fname varchar2[20], lname varchar2[20], age int)')
db.execute('insert into tests values("Karthik", "Chandu", 21)')
db.commit()
cursor = db.execute('select * from tests')
for row in cursor:
	print dict(row)

db1 = sqlite3.connect('test1.db')
db1.execute('drop table if exists tests')
db1.row_factory = sqlite3.Row
db1.execute('create table tests(fname varchar2[20], lname varchar2[20], age int)')
db1.execute('insert into tests values("Karthik", "Chandu", 21)')
db1.commit()
cursor1 = db1.execute('select * from tests')
for row in cursor1:
	print dict(row)