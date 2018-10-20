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
		self.cost = cost
		self.depth = 0 if parent is None else parent.depth + 1
	
	
	def __lt__(self, other):
		return self.cost < other.cost
	
	
	def get_route(self):
		"""
		Backtrack to get the route to this node.
		
		Return:
		  A list of Location to this node, including this node.
		"""
		
		route = []
		
		n = self
		while n is not None:
			route.insert(0, n.state)
			n = n.parent
		
		return route
