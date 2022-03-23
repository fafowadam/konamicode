#link.py

def link(src=None,comp_class=None,map_rows=None):

			
	def check_pipes(src,map_rows):
	
		src_pipes = tuple(src.pipe.keys())
		map_pipes = tuple(map_rows.keys())
		
		if map_pipes != src_pipes:
		
			raise ValueError

	check_pipes(src,map_rows)
	
	inputs = list(map_rows.values())
	comp = comp_class()
	comp.interval = {}
	comp_name = type(comp).__name__
	src.pipe.update({comp_name:comp})

	for pipe in src.pipe:
		
		try:
			intervals = list(src.pipe[pipe].interval.keys())
		except AttributeError: pass
		
		for interval in intervals:
		
			inputs = map_rows.values()
			comp = comp_class(inputs=inputs)
			comp.name = interval
			src.pipe[comp_name].interval.update({interval:comp})
			

	intervals = list(src.pipe[comp_name].interval.keys())
	pipes = list(src.pipe.keys())
	inputs = list(map_rows.values())

	for interval in intervals:
	
		target = src.pipe[comp_name].interval[interval]
		
		for pipe in pipes:
		
			if pipe != comp_name:
			
				src.pipe[pipe].interval[interval].outputs.append((target,map_rows[pipe]))
					
					
				
	#quit()