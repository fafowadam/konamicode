#DataPipe.py
from data_frame import DataFrame
	
	
class DataPipe:

	def __init__(self,intervals,df_class=DataFrame):
	
		self.intervals = sorted(intervals)
		
		#2. Create a object that is a member of a DataFrame class for each interval
		keys = {}
		for interval in self.intervals:
			keys.update({interval:df_class(interval)})
		self.intervals = keys
		
		#3. Link the DataFrame objects together such that the output of each interval cascased into
		#	The input of the next
		is_root = True # Needed so we don't try to back-link the first DataFrame in the list
		last = None # Holds a ref to the previous DataFrame in the list
		for interval in self.intervals:
			if is_root:
				root = self.intervals[interval] # Will use this below as the entry point to the pipe
				is_root = False # Subsequent DataFrames can not be the root.
				last = interval
				continue
			else:
				self.intervals[last].chain.append(self.intervals[interval].append)
				self.intervals[interval].step = self.intervals[last].limit
				last = interval
				
		#4. Set the input of the first DataFrame interval as the entry point for the whole chain. 
		self.append = root.append