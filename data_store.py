#data_store.py
import sqlite3 as db



class DBWriter():

	def __init__(self):
	
		self.conn = db.connect('price_data.db')
		self.cursor = self.conn.cursor()
		
		SQL_INIT_TABLE = '''

			CREATE TABLE IF NOT EXISTS
			candles(interval TEXT, time INT, high FLOAT, low FLOAT, open FLOAT, close FLOAT)

		'''

		self.cursor.execute(SQL_INIT_TABLE)
		self.max_time = self.max_time()
		
	def write(self,rows):
		
		for candle in rows:
		
			values = tuple(candle)

			SQL_INSERT_RECORD = f"INSERT INTO candles VALUES {values}"
			self.cursor.execute(SQL_INSERT_RECORD)
			
			self.conn.commit()
			
	def max_time(self):
	
		max_time = self.cursor.execute("""SELECT MAX(time) FROM CANDLES""").fetchone()[0]
		
		if max_time == None:
			max_time = 0
		return max_time
		

	def load_partials(self,intervals):

		conn = db.connect('price_data.db')
		cursor = conn.cursor()
		intervals = list(intervals.keys())
		data = []

		def load_interval(interval):
		
			my_index = intervals.index(interval)
			prev_index = my_index - 1
			prev_int = intervals[prev_index]
			
			query = f"SELECT MAX(time) FROM candles WHERE interval IS '{interval}' "
			last_time = cursor.execute(query).fetchone()[0]
			if last_time is None: last_time = 0
			
			query = f"SELECT * FROM candles WHERE INTERVAL IS '{prev_int}' "
			query += f"AND time > {last_time}"
			
			results = cursor.execute(query).fetchall()
			return results
			
		[data.extend(load_interval(interval)) for interval in reversed(intervals)]
		
		return data
		

				



if __name__ == "__main__":
#Test code...

	intervals = {'1m':60,'5m':5,'15m':3,'1h':4,'6h':6,'1d':4}
	print(load_partials(intervals))