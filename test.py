#vector

class Vector:

	def __init__(self,rows,cols):
	
		self.matrix = []
		
		for row in range(rows):

			self.matrix.append([])
			
			for col in range(cols):
			
				self.matrix[row].append((row,col))
				
rows = ['High','Low','Open','Close']			
cols = {'1m':60,'5m':5,'15m':3,'1h':4,'6h':6,'1d':4}

candle = ('1m',42800,87.7,78.4,81.67,79.4)
interval = candle[0]

start = 2

candle = candle[start:]
z = zip(rows,candle)

for _ in z:
	
	row,x = _
	
	print(f"loading value {x} into row '{row}', column '{interval}'")




