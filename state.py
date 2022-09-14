import copy

### An abstract class that other states will inherit from.
class State:
    def __init__(self):
        pass
    def isGoal(self):
        pass
    def successors(self):
        pass
    def __repr__(self):
        pass
