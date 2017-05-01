from scanner import Token


class Expr:
    pass


class Unary(Expr):
    def __init__(self, operator, right):
        assert isinstance(operator, Token)
        assert isinstance(right, Expr)

        self.operator = operator
        self.right = right

    def accept(self, visitor):
        return visitor.visitUnary(self)


class Binary(Expr):
    def __init__(self, left, operator, right):
        assert isinstance(left, Expr)
        assert isinstance(operator, Token)
        assert isinstance(right, Expr)

        self.left = left
        self.operator = operator
        self.right = right

    def accept(self, visitor):
        return visitor.visitBinary(self)


class Grouping(Expr):
    def __init__(self, expression):
        assert isinstance(expression, Expr)

        self.expression = expression

    def accept(self, visitor):
        return visitor.visitGrouping(self)


class Literal(Expr):
    def __init__(self, value):
        assert isinstance(value, object)

        self.value = value

    def accept(self, visitor):
        return visitor.visitLiteral(self)

