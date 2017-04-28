#! /usr/local/bin/python3

from out.Expr import *
from scanner import Token, TokenType

class AstPrinter:
    def printast(self, expr):
        return expr.accept(self)

    def visitBinary(self, expr):
        return self.parenthesize(expr.operator.lexeme, expr.left, expr.right)

    def visitGrouping(self, expr):
        return self.parenthesize("group", expr.expression)

    def visitLiteral(self, expr):
        return str(expr.value)

    def visitUnary(self, expr):
        return self.parenthesize(expr.operator.lexeme, expr.right)

    def parenthesize(self, name, *exprs):
        string = "(" + name

        for expr in exprs:
            string += " "
            string += expr.accept(self)

        string += ")"

        return string

if __name__ == "__main__":
    expression = Binary(
        Unary(
            Token(TokenType.MINUS, "-", None, 1),
            Literal(123)),
        Token(TokenType.STAR, "*", None, 1),
        Grouping(
            Literal(45.67)))
    print(AstPrinter().printast(expression))