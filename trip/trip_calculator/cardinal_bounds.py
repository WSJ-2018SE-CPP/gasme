
class CardinalBounds:
    """
    Class to represent the N, S, E and W bounds of locations
     represented as longitude and latitude coordinates.
    """
    
    def __init__(self, N, S, E, W):
        """
        Args:
          N - the max latitude
          S - the min latitude
          E - the max longitude
          W - the min longitude
        """
        self.N = N
        self.S = S
        self.E = E
        self.W = W
        
