import sympy as sy
x,y=sy.symbols("同学 苹果")
a=sy.solve([3*x+11-y,4*x-1-y],[x,y])
print(a)