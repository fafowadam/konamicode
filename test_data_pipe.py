#test_data_pipe
from line_graph import LineGraph as lg
from data_frame import DataFrame as df
from data_pipe import DataPipe as dp
import statistics

class Mean(df):

	def calc(self):
	
		return statistics.mean(self.data)
		
class Median(df):

	def calc(self):
	
		pass
	
class Distribution(df):

	def calc(self):
	
		pass

# LineGraph generator		
g = lg()

# DataPipe object
p = dp(pclass=Mean,intervals={'m':60,'h':60,'d':24,'y':365})
p.pipe['d'].outputs.append(print)

for _ in range(10**8):

	p.append(g.nextx())