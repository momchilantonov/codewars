"""
Your task is to write a higher order function for chaining together
a list of unary functions. In other words, it should return a function
that does a left fold on the given functions.
"""


def f1(x): return x*2
def f2(x): return x+2
def f3(x): return x**2
def f4(x): return x.split()
def f5(x): return [i[::-1].title() for i in x]
def f6(x): return "_".join(x)


def chained(functions):
    def apply(param):
        result = param
        for f in functions:
            result = f(result)
        return result
    return apply


# TESTS
assert chained([f1, f2, f3])(0) == 4
assert chained([f1, f2, f3])(2) == 36
assert chained([f3, f2, f1])(2) == 12
assert chained([f4, f5, f6])("lorem ipsum dolor") == "Merol_Muspi_Rolod"
