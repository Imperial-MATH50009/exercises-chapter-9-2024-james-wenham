"""Implement classes of nodes."""
import numbers


class Expression:
    """Base class for all tree nodes."""

    def __init__(self, *operands):
        self.operands = operands 

    def __add__(self, other):

        if isinstance(other, Expression):
            return Add(self, other)
        elif isinstance(other, numbers.Number):
            return Add(self, Number(other))
        else:
            raise ValueError("Not valid data type")

    def __radd__(self, other):
        if isinstance(other, Expression):
            return Add(other, self)
        elif isinstance(other, numbers.Number):
            return Add(Number(other), self)
        else:
            raise ValueError("Not valid data type")

    def __sub__(self, other):
        if isinstance(other, Expression):
            return Sub(self, other)
        elif isinstance(other, numbers.Number):
            return Sub(self, Number(other))
        else:
            raise ValueError("Not valid data type")

    def __rsub__(self, other):
        if isinstance(other, Expression):
            return Sub(other, self)
        elif isinstance(other, numbers.Number):
            return Sub(Number(other), self)
        else:
            raise ValueError("Not valid data type")

    def __mul__(self, other):
        if isinstance(other, Expression):
            return Mul(self, other)
        elif isinstance(other, numbers.Number):
            return Mul(self, Number(other))
        else:
            raise ValueError("Not valid data type")

    def __rmul__(self, other):
        if isinstance(other, Expression):
            return Mul(other, self)
        elif isinstance(other, numbers.Number):
            return Mul(Number(other), self)
        else:
            raise ValueError("Not valid data type")

    def __truediv__(self, other):
        if isinstance(other, Expression):
            return Div(self, other)
        elif isinstance(other, numbers.Number):
            return Div(self, Number(other))
        else:
            raise ValueError("Not valid data type")

    def __rtruediv__(self, other):
        if isinstance(other, Expression):
            return Div(other, self)
        elif isinstance(other, numbers.Number):
            return Div(Number(other), self)
        else:
            raise ValueError("Not valid data type")

    def __rpow__(self, other):
        if isinstance(other, Expression):
            return Pow(other, self)
        elif isinstance(other, numbers.Number):
            return Pow(Number(other), self)
        else:
            raise ValueError("Not valid data type")

    def __pow__(self, other):
        if isinstance(other, Expression):
            return Pow(self, other)
        elif isinstance(other, numbers.Number):
            return Pow(self, Number(other))
        else:
            raise ValueError("Not valid data type")


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
        return (" " + self.symbol + " ").join(lis1)


class Terminal(Expression):
    """Base class for termnial nodes."""

    prec = 5

    def __init__(self, value):
        """Call expression class to say that operands is empty."""
        super().__init__()
        self.value = value

    def __repr__(self):
        return repr(self.value)

    def __str__(self):
        return str(self.value)


class Add(Operator):
    """Addition node."""

    symbol = "+"
    prec = 1


class Sub(Operator):
    """Subtraction node."""

    symbol = "-"
    prec = 1


class Mul(Operator):
    """Multiplication node."""

    symbol = "*"
    prec = 2


class Div(Operator):
    """Division node."""

    symbol = "/"
    prec = 3


class Pow(Operator):
    """Exponent node."""

    symbol = "^"
    prec = 4


class Symbol(Terminal):
    """Initialise symbol data type."""

    def __init__(self, value):
        super().__init__(value)
        if not isinstance(self.value, str):
            raise ValueError(f"Symbol value should be string not {type(self.value)}")


class Number(Terminal):
    """Initialise number data type."""

    def __init__(self, value):
        super().__init__(value)
        if not isinstance(self.value, numbers.Number):
            raise ValueError(f"Number value should be number not {type(self.value)}")