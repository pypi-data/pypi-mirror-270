from pybigdata import optimization as OPT

x_0 = 1
def df(x): return 5 * (x + 3)


OPT.simple_gradient_descent(df, x_0)
