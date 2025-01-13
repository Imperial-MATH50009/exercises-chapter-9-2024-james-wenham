"""Implement classes of nodes."""


class Expression:
    """Base class for all tree nodes."""

    def __init__(self, *operands):
        self.operands = operands 

    def __add__(self, other):
        return Add(self, other)

    def __sub__(self, other):
        return Sub(self, other)

    def __mult__(self, other):
        return Mult(self, other)

    def __truediv__(self, other):
        return Div(self, other)

    def __pow__(self, other):
        return Pow(self, other)


class Operator(Expression):
    """Define operator class."""

    def __repr__(self):
        return type(self).__name__ + repr(self.operands)

    def __str__(self):
        lis1 = []
        for i in self.operands:
            if self.prec > i.prec:
                lis1.append("(" + i.__str__() + ")")
            else:
                lis1.append(i.__str__())
        return self.symbol.join(lis1)


class Terminal(Expression):
    """Base class for termnial nodes."""

    prec = 0

    def __init__(self, value):
        """Call expression class to say that operands is empty."""
        super().__init__()
        self.value = value

    def __repr__(self):
        return repr(self.value)

    def __str__(self):
        return str(self.value)


class Add(Operator(Expression)):
    """Addition node."""

    symbol = "+"
    prec = 1


class Sub(Operator(Expression)):
    """Subtraction node."""

    symbol = "-"
    prec = 1


class Mult(Operator(Expression)):
    """Multiplication node."""

    symbol = "*"
    prec = 2


class Div(Operator(Expression)):
    """Division node."""

    symbol = "/"
    prec = 3


class Pow(Operator(Expression)):
    """Exponent node."""

    symbol = "**"
    prec = 4

class Symbol(Terminal(Expression)):
    