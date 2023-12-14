import sympy
from sympy import solve

import math

def sqrt(x):
    return math.sqrt(x)

a = float(eval(input("a: ")))
b = float(eval(input("b: ")))
c = float(eval(input("c: ")))

dadt = input("da/dt (x if find): ")
dbdt = input("db/dt (y if find): ")
dcdt = input("dc/dt (z if find): ")

def find(a,b,c,dadt,dbdt,dcdt) -> int:

    if round(a**2 + b**2,2) != round(c**2,2):
        raise ArithmeticError("Not a valid traingle")

    rate:int = None

    print(rate:=round(solve(f"{c}*{dcdt}-{b}*{dbdt}-{a}*{dadt}")[0],2))

    return rate

find(a,b,c,dadt,dbdt,dcdt)
