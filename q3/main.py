# all imports below

"""
Any extra lines of code (if required)
as helper for this function.
"""

def findDelay(dist):
	'''
	Parameters
	----------
	dist : A `float`
	
	
	Returns
	-------
	A `float`
	'''
	R=dist
	G=6.674/1e11
	c=2.998*1e8
	M=6357000
	time_delay=((R/c)*(pow(1-((G*M)/(R*c*c)),0.5)))
	return float(time_delay)
