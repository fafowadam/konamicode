import statistics
from data_frame import DataFrame as df

class Open(df):

	def calc(self):
	
		return self.data[0]
		
class Close(df):

	def calc(self):
	
		return self.data[len(self.data) - 1]
		
class High(df):

	def calc(self):
	
		return max(self.data)
		
class Low(df):

	def calc(self):
	
		return min(self.data)