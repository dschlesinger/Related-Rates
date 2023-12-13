import sympy
from sympy import solve

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

dadt = input("da/dt (x if find): ")
dbdt = input("db/dt (y if find): ")
dcdt = input("dc/dt (z if find): ")

def find(a,b,c,dadt,dbdt,dcdt) -> int:

    rate:int = None

    print(rate:=round(solve(f"{c}*{dcdt}-{b}*{dbdt}-{a}*{dadt}")[0],2))

    return rate

find(a,b,c,dadt,dbdt,dcdt)
