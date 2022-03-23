#DataMatrix.py

#import inspect
from data_frame import DataFrame
from data_pipe import DataPipe
from composite_pipe import CompositePipe

class DataMatrix:

	def __init__(self,pipes,intervals,cp_class=CompositePipe,stream=DataFrame):
	
		#Requirements
		#1. Create a set of DataPipe objects, given a list of DataPipe classes.
	
		self.pipes = {}
		
		# Default classes. These should be over-ridden in sub classes.
		self.cp_class = CompositePipe
		self.composite_out = DataFrame

		for pipe in pipes:

			self.pipes.update({pipe:DataPipe(intervals,df_class=pipe)})
		
		# A composite output of the CompositePipes for each column...
		self.pipes.update({'Composite':stream(1)})
	
	
		#2. Link each column (intervals) from each pipe vertically, so that a composite output
		#	can be obtained for each. 

		# Create a new index to store the column linkage, same as
		# we did above for creating and index of DataPipes (rows)
		self.intervals = {}
		inputs = set(self.pipes.keys())
	
		# Initialize the intervals index...
		for interval in sorted(intervals):
		
			self.intervals.update({interval:[]})
		
		# Fill the index with DataFrame refs from DataPipe.
		for interval in self.intervals:

			for pipe in self.pipes:
				
				if pipe == 'Composite': continue
				df = self.pipes[pipe].intervals[interval]
				self.intervals[interval].append({pipe:df})
			
			# Need to do this as a list to keep the keys in order
			inputs = list(self.pipes.keys())
			
			# Create our CompositePipes to catch the output of each column
			cp = cp_class(inputs)
			cp.chain.append(self.pipes['Composite'].append)
			self.intervals[interval].append({'Composite':cp})
		
		# Wire up the output of each DataFrame type for each interval to its
		# Corresponding CompositePipe...
		for interval in self.intervals:
		
			pipes = self.intervals[interval]
			# target is the CompositePipe for each column to wire inputs to...
			target = list(self.intervals[interval][-1].values())[0]
			
			for row in pipes:
			
				df_class = list(row.keys())[0]
				df_ref = list(row.values())[0]
				
				if df_class == 'Composite':	pass
				else:
					df_ref.chain.append(target.append)
					
					
					
	def append(self,val):
	
		for pipe in self.pipes:
		
			if pipe == 'Composite': continue
			self.pipes[pipe].append(val)
				
	
	
	




