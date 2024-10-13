import sympy
from sympy import solve, symbols

import math

def sqrt(x):
    return math.sqrt(x)

def find() -> float:

    # sympy vars

    x, y, z = symbols('x y z')

    # eval() so can use sqrt(), please do not hack 🙏
    a = float(eval(input("a: ")))
    b = float(eval(input("b: ")))

    hyp = input("c (s if solve for hyp): ")
    c = sqrt(a**2 + b**2) if hyp == 's' else float(hyp)

    dadt = eval(input("da/dt (x if find): "))
    dbdt = eval(input("db/dt (y if find): "))
    dcdt = eval(input("dc/dt (z if find): "))

    if round(a**2 + b**2,2) != round(c**2,2):
        raise ArithmeticError("Not a valid traingle")

    print(rate:=solve(f"{c}*{dcdt}-{b}*{dbdt}-{a}*{dadt}")[0])

    return rate

if __name__ == '__main__':
    find()
