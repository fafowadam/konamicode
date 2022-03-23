#DataFrame
#Requirements:

from copy import copy

class DataFrame:

	def __init__(self,limit,step=1,data_type=float):
	
		#Define the size of the dataframe
		self.limit = limit
		
		# Count to limit by step increments.
		self.step = step
		
		# Starting cycle counter position.
		self.count = 0
		
		# To keep track of time
		self.cycle = 0
		self.time = 0
		
		# For validating input on append method...
		self.input_type = data_type
		
		# Initialize the output to the correct data type
		self.output = data_type()
		
		# A list of functions to called and
		# passed the output once the limit has been reached. 
		self.chain = []
		self.outputs = []
		
	def append(self,x):
			
		if type(x) is self.__class__:
		
			x = x.output
		
		if self.count == self.limit:
		
			self.calc_limit()
			
			# Output the result of its calculation.
			[output(copy(self)) for output in self.chain]
			[output(self.output) for output in self.outputs]
			
			self.reset_cycle()
			
		self.calc_step(x)
		self.count += self.step
			
	def reset_cycle(self):
	
		self.count = 0
		self.cycle += 1
		self.time = self.limit * self.cycle
		
	def calc_step(self,x):
	#Perform an optional action on each new value
	
		pass
		
	def calc_limit(self):
	# Perform a calculation or some action when the limit has been reached.
	
		pass
		

if __name__ == "__main__":


	class Test(DataFrame):
	
		def calc_step(self,val):
		
			print(f"step count: {self.count}")
			
		def calc_limit(self):
		
			print(f"limit count: {self.count}")
			
	test = Test(10)
	
	for _ in range(100):
	
		test.append(1)
		


	