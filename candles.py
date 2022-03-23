# candles.py

# Imports for the DataMatrix structure
# and supporting classes
from data_frame import DataFrame
from composite_pipe import CompositePipe
from data_matrix import DataMatrix

# Data generator to be used as input values
from line_graph import LineGraph

# Data points to be tracked
from data_points import High
from data_points import Low
from data_points import Open
from data_points import Close

# Create the data generator
x = LineGraph()

# Define the params for the DataMatrix
pipes = [High,Low,Open,Close]
intervals = {60, 300, 900, 3600, 21600, 86400}

# Sublcass CompositePipe and DataFrame 
# to modify the column and composite outputs

class Candle(CompositePipe):

	def calc(self,inputs):
		"""
		Returns an aggregated dict of just the output values for each
		defined input, along with the limit and timestamp for each input
		for identifiers
		"""
		
		interval = inputs[0].limit
		time = inputs[0].time

		candle = {
			"interval":interval,
			"time":time
		}
		
		for inp in inputs:
			
			key = inp.__class__.__name__
			candle.update({key:inp.output})
			
		return candle
		
class CandleStream(DataFrame):
	"""
	Recieves candles from CandleClass, FIFO, and simply passes them
	back out. Convenience class so that we don't have to manually
	wire up the outputs of each Candle interval to an output.
	"""

	def calc_step(self,inp):
	
		self.output = inp.output

def print_interval(interval):

	if interval["interval"] == 86400: print(interval)

# Create the DataMatrix and send its composite output to print		
candles = DataMatrix(pipes,intervals,cp_class=Candle,stream=CandleStream)
candles.pipes['Composite'].outputs.append(print_interval)

# Feed it data...
while True:

	candles.append(x.nextx())