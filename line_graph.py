#LineGraph Generator

import random
	
class LineGraph:

	def __init__(self,start=None):
	
		self.value_range = (10,101)
		self._init_run(start)
		self.x = self.start
		
		
	def _init_run(self,start=None):
	
		if start:

			self.start = start
			
		else:
		
			self.start = random.randrange(*self.value_range)
			
		self.end = random.randrange(*self.value_range)
		
		#3. Determine length of run and direction
		self.diff = self.end - self.start
		self.run = abs(self.diff)
		
		try:
			self.direction = self.diff/self.run
		except ZeroDivisionError:
			self.direction = random.choice([-1,1])
		
		
	def nextx(self):
	
		rv = self.x
		
		if self.x == self.end: self._init_run(start=self.end)
		else: self.x += self.direction
		
		return rv
		
		
if __name__ == "__main__":
		
	graph = LineGraph()

	while True:

		x = graph.nextx()
		print(x)
