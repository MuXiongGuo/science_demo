# 解微分方程
from sympy import *
f = symbols('f', cls=Function)#定义函数标识符
x = symbols('x')#定义变量
s = symbols('s')#定义变量
eq = Eq(diff(f(x),x,1),0.0419*x*(1-x*4000)-0.0047*s*x)#构造等式，即dy/dx=y
#diff(函数,自变量,求导次数)
print(dsolve(eq, f(x)))
pprint(dsolve(eq, f(x)))#以"pretty"形式打印方程的解
