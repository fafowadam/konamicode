import random

class LineGraph:

	"""
	Version 1
	
	Creates object representing a line graph.
	Single method nextx() to return next x value
	in the line graph
	"""

	def __init__(self,start=None):
	
		self.floor = 10
		self.ceil = 100
		
		if start:
			self.x = start
		else:
			self.x = random.randrange(self.floor,self.ceil)
		self.rise = (random.choice([-1,1]) * random.randrange(1,100))
		self.run = self.rise_run()
		
		try:
		
			self.increment = round(self.rise/self.run,4)
			
		except ZeroDivisionError:
		
			self.__init__(start)

	def rise_run(self,start=None,direction=None):
	
		#initialize the slope...

		# range of possible values
		self.r = (300,86400)
		# start point for slope
		if start: self.s = start
		else: self.s = random.randrange(*self.r)
		# end point for slope
		self.e = random.randrange(*self.r)
		# direction of change
		if direction:
			self.d = direction
		else:
			self.d = (self.e - self.s)
			# prevent divide by zero
			if self.d != 0:	self.d = self.d/abs(self.d)
			else: self.d = 1
		
		self.i = self.s
		
		return abs(self.s - self.e)
		
	def nextx(self):
	
		rv = round(self.x,4)

		change = round((self.increment + random.randrange(0,10)*random.choice([-1,1]))/100,3)
		
		if self.x + change <= self.floor:
			
			self.rise_run(direction=1)
			return rv
			
		if self.x + change >= self.ceil:
			
			self.rise_run(direction=-1)
			return rv
		
		self.x += change
		self.i += self.d

		
		# If we reached the stop point for the run,
		# reset...
		if ((self.d < 0 and self.i <= self.e)
			or (self.d > 0  and self.i >= self.e)):
			
			self.rise_run(start=self.i)
			
		if self.x < 0:
		
			print(f"{self.x} ... fuck. again.")
		
		return rv		


if __name__ == '__main__':
# Test code...

	lg = LineGraph()
	for _ in range(10**6):

		print(lg.nextx())
