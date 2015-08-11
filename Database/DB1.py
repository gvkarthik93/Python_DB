import sqlite3

db = sqlite3.connect('test1.db')
db.execute('drop table if exists tests')
db.row_factory = sqlite3.Row
db.execute('create table tests(fname text, age int)')
db.execute('insert into tests values("Karthik", 21)')
db.commit()
cursor = db.execute('select age, fname from tests order by fname')
for row in cursor:
	print dict(row)