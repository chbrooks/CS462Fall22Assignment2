
from state import State

## A State for the Fox and Chickens problem. We have four instance variables, representing the four objects.
##  (fox, chicken, grain, boat). Values for them are {'left','right'}"""

class FoxAndChickensState(State):
    def __init__(self, f='left', c='left', g='left', b='left', parent=None):
        self.fox = f
        self.chicken = c
        self.grain = g
        self.boat = b
        self.parent = parent

    def isGoal(self):
        return self.fox == 'right' and self.chicken == 'right' and self.grain == 'right' and self.boat == 'right'

    ## check to make sure that we have not left the fox with the chicken, or the chicken with the grain
    def isValidState(self):
        if self.fox == self.chicken and self.fox != self.boat:
            return False
        if self.chicken == self.grain and self.grain != self.boat:
            return False
        return True

    def __repr__(self):
        return "fox: %s chicken: %s grain: %s boat: %s" % (self.fox, self.chicken, self.grain, self.boat)

### generate all valid successor states, and return them in a list.
    def successors(self):
        successorStates = []
        if self.fox == self.boat:
            s = FoxAndChickensState(flip(self.fox), self.chicken, self.grain, flip(self.boat), self)
            if s.isValidState():
                successorStates.append(s)
        if self.chicken == self.boat:
            s = FoxAndChickensState(self.fox, flip(self.chicken), self.grain, flip(self.boat), self)
            if s.isValidState():
                successorStates.append(s)
        if self.grain == self.boat:
            s = FoxAndChickensState(self.fox, self.chicken, flip(self.grain), flip(self.boat), self)
            if s.isValidState():
                successorStates.append(s)
        s = FoxAndChickensState(self.fox, self.chicken, self.grain, flip(self.boat), self)
        if s.isValidState():
            successorStates.append(s)
        return successorStates

## helper function to handle changing left to right.
def flip(side):
    if side == 'left':
        return 'right'
    else:
        return 'left'