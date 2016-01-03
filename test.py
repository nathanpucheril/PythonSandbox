class Expression(object):
    def __init__(self, terms, var = "x"):
        assert isinstance(terms, list), "Terms must be a list of tuples"
        assert isinstance(var, str), "The Variable must be a string representing the Variable"
        self.var = var
        self.terms = terms

class Fraction(Expression):

    def __init__(self, num, den):
        self.num = num

    @staticmethod
    def _fractifyExpression(e):
        if Fraction.isFraction(e):
            return e
        return Fraction(e, Expression.make_constant(1))

print(Fraction._fractifyExpression)
