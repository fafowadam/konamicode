import inspect
from copy import copy

class CompositePipe:

	"""
	CompositePipe pipe enables ability to link DataFrames within
	columns within a DataMatrix, analogously to how DataPipe links 
	DataFrames within a row.
	"""

	def __init__(self,inputs):

		self.inputs = {}
		self.chain = []
		self.outputs = []
	
		#Requirements:
		#1. Create a object attribute for each item in inputs
		[self.inputs.update({inp:None}) for inp in inputs]
			
		#2. When each input is recieved, check to see if all inputs been received
		#	If so, do any needed processing and output

	
	def append(self,inp):
	# Receive and process inputs...

		# inp should be a DataFrame instance. Its class type
		# is checked against the input mapping to see if it
		# is an input.
		input = inp.__class__
		if input in set(self.inputs.keys()):
		
			self.inputs[input] = inp
		
		else:
		# If the class type does match an input mapping...
			raise TypeError
			
			
		# Check if all inputs have been received...
		inputs = []
		vals = []
		
		# Skip the Composite row...
		for inp in self.inputs.keys():
			if inp != "Composite": inputs.append(inp)
		
		for inp in inputs:
		# Still missing inputs if any are set to None
			
			val = self.inputs[inp]
			if val == None: return
			else: vals.append(val)
			
		# All inputs have been received, process and output them
		self.output = self.calc(vals)
		
		# Output to the outputs list...
		for output in self.chain:
			
			output(copy(self))
		
		for inp in self.inputs:
		
			self.inputs[inp] = None
				
	
	def calc(self,vals):
	
		return vals
				