import sqlite3

def insert(db, row):
	db.execute('insert into test2 values (?,?)',(row['t1'],row['i1']))
	db.commit()

def retrieve(db,t1):
	cursor = db.execute('select * from test2 where t1 = ?',(t1,))
	return cursor.fetchone()

def update(db,row):
	db.execute('update test2 set i1 = ? where t1 = ?',(row['i1'],row['t1']))
	db.commit()

def delete(db,t1):
	db.execute('delete from test2 where t1 = ?',(t1,))
	db.commit()

def disp_rows(db):
	cursor = db.execute('select * from test2 order by t1')
	for row in cursor:
		print "'{}:{}'.format(row['t1'],row['i1'])"

def main():
	db.sqlite3.connect('test2.db')
	db.row_factory =  sqlite3.Row
	print "Create table test2"
	db.execute('drop table if exists test2')
	db.execute('create table test2(t1 text, i1 int)')

	print "Create rows"
	insert(db,dict(t1 = "one", i1 = 1))
	insert(db,dict(t1 = "two", i1 = 2))
	insert(db,dict(t1 = "three", i1 = 3))
	insert(db,dict(t1 = "four", i1 = 4))
	disp_rows(db)

	print "Retrieve rows"
	print dict(retrieve(db,'one')), dict(retrieve(db,'two'))

	print "Update rows"
	update(db, dict(t1 = 'one', i1 = 101))
	update(db, dict(t1 = 'three', i1 = 103))
	disp_rows(db)

	print "Delete rows"
	delete(db, 'one')
	delete(db, 'three')
	disp_rows(db)