from trip.location import Location

class Node:
	"""
	A Node class for A* Search.
	"""
	
	def __init__(self, state, parent, cost):
		"""
		Initializes the Node.
		
		Args:
		  state: the location
		  parent: the parent Node
		  cost: the cost from parent
		"""
		
		self.state = state
		self.parent = parent
		self.cost = 0 if parent is None else parent.cost + cost
		self.depth = 0 if parent is None else parent.depth + 1
		
