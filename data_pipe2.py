#DataPipe.py
from data_frame2 import DataFrame
	
	
class DataPipe:

	def __init__(self,intervals,df_class = DataFrame):
	
		self.intervals = sorted(intervals)
		
		#2. Create a object that is a member of a DataFrame class for each interval
		keys = {}
		for interval in self.intervals:
			keys.update({interval:df_class(interval)})
		self.intervals = keys
		
		#3. Link the DataFrame objects together such that the output of each interval cascased into
		#	The input of the next
		is_root = True
		last = None
		for interval in self.intervals:
			if is_root:
				root = self.intervals[interval]
				is_root = False
				last = interval
				continue
			else:
				self.intervals[last].outputs.append(self.intervals[interval].append)
				self.intervals[interval].step = self.intervals[last].limit
				last = interval
				
		#4. Set the input of the first DataFrame interval as the entry point for the whole chain. 
		self.append = root.append


if __name__ == "__main__":
#Test code...

	from line_graph2 import LineGraph
	
	g = LineGraph()
	
	dp = DataPipe({60, 300, 900, 3600, 21600, 86400})
	dp.intervals[900].outputs.append(print)
	
	for _ in range(10000):
		dp.append(g.nextx())