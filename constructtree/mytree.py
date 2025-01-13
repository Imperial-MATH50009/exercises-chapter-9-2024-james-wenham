"""Practice building my own tree class."""


class MTreeNode():
    """Node for tree."""

    def __init__(self, value, *children):
        """Value of node and pointer to tuple of child nodes."""
        self.value = value
        self.children = children

def mpostvisitor(tree, fn):
    
    return fn(*(mpostvisitor(i) for i in tree.children))

#base class test:

class Base1():
    """Test for how abstract base classes work."""

    def __init__(self, *value):
        self.value = value 

    def __add__(self,other):
        return Add(self, other)

class Add(Base1):
    """Now look at the tuple of values which are base1 classes!"""
    #put in an attribute for the symbol


    