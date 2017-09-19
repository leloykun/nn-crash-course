from sympy import *

acceptable_delta = 0.000001

if __name__ == '__main__':
    x = Symbol('x')
    func = sympify(input("f(x) = "), evaluate = False)
    derv = simplify(diff(func, x))
    print("f'(x) = ", derv)
    print()

    x_val = float(input("initial x value: "))
    learning_rate = float(input("learning rate: "))
    print()

    # gradient descent helps us find a minima
    # of a function starting from an arbitrary
    # initial x value
    last_y = func.evalf(10, subs={x: x_val})
    print("     x        f(x)")
    print("%10.6f" % x_val, "%10.6f" % last_y)

    for i in range(1, 10000):
        # TODO: explain why this works
        # (basically, we're just incrementally 
        #  going down the tangent of a curve)
        # (like, x := x - learning rate * slope of tangent)
        x_val -= learning_rate * derv.evalf(10, subs={x : x_val})
        y = func.evalf(10, subs={x: x_val})
        print("%10.6f" % x_val, "%10.6f" % y)

        if abs(last_y - y) < acceptable_delta:
            print("a minima is found @ around (%.6f, %.6f)" % (x_val, y))
            print("in", i, "timesteps")
            print()
            break

        last_y = y

    print("critical points are at:")
    x_crits = solve(derv, x)
    for x_crit in x_crits:
        y_crit = func.evalf(10, subs={x: x_crit})
        print("(%.6f, %.6f)" % (x_crit, y_crit))

    # TODO improve this visualization
    plot(func, (x, -10, 10))
