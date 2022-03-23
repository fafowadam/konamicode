#DataPoints.py

from data_frame import DataFrame as df

class High(df):

	def calc_step(self,val):
	
		if self.count == 0 or val > self.output:
		
			self.output = val
	
class Low(df):

	def calc_step(self,val):
	
		if self.count == 0 or val < self.output:
		
			self.output = val
	
class Open(df):

	def calc_step(self,val):
	
		if self.count == 0:
		
			self.output = val
	
class Close(df):

	def calc_step(self,val):
	
		self.output = val
	