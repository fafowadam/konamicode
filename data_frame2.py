#DataFrame
#Requirements:

class DataFrame:

	def __init__(self,limit):
	
		#Define the size of the dataframe
		self.limit = limit
		self.data = []
		self.count = 0
		self.outputs = []
		
	def append(self,x):
	
		self.calc_step(x)
		self.count += 1
		if self.count == limit:
		
			self.calc_limit()
			
			#Outout the result of its calculation.
			[output(self) for output in self.outputs]
			self.count = 0
			self.data.clear()
		
	def calc_step(self,x):
	#Perform an optional action on each new value
	
		self.data.append(x)
		
	def calc_limit(self):
	#Perform a calculation or some action when the limit has been reached.
	
		self.result = self.data

if __name__ == "__main__":

	from line_graph2 import LineGraph
	import statistics
	
	class Mean(DataFrame):
	
		def calc_limit(self):
		
			self.result = statistics.mean(self.data)
			

	limit = 60
	df = Mean(limit)
	df.outputs.append(print)
	g = LineGraph()
	
	for _ in range(limit + 1):
	#Input values into the dataframe until its limit is reached.
	
		df.append(g.nextx())
	
	