import sqlite3
from sqlite3 import Error
import os.path


class DBM:
	
	dbName = None
	
	def __init__(self, dbName):
		self.dbName = dbName

	def dbExists(self):
		if(not os.path.exists(self.dbName)):
			return False
		else:
			return True

	def createDB(self):
		try:
			conn = sqlite3.connect(self.dbName)
			c = conn.cursor()
			c.execute('CREATE TABLE measures (id INTEGER PRIMARY KEY AUTOINCREMENT, temperature INTEGER, humidity INTEGER, timestamp INTEGER)')
			conn.commit()	
			print "Database file created..."

		except Error as e:
			print(e)
		finally:
			conn.close()
			
	def insertRecord(self, temp, hum, tmstmp):
		try:
			conn = sqlite3.connect(self.dbName)
			c = conn.cursor()
			c.execute('INSERT INTO measures (temperature, humidity, timestamp) VALUES (%d, %d, %d)' % (temp, hum, tmstmp))
			conn.commit()	
			
			print "Record inserted..."

		except Error as e:
			print(e)
		finally:
			conn.close()
		
	def getLastRecord(self):
		try:
			conn = sqlite3.connect(self.dbName)
			c = conn.cursor()
			c.execute('SELECT * FROM measures ORDER BY timestamp DESC LIMIT 1')
			
			rows = c.fetchall()
			
			conn.commit()	
		except Error as e:
			print(e)
		finally:
			conn.close()
		
		
		return rows[0][0], rows[0][1], rows[0][2], rows[0][3]