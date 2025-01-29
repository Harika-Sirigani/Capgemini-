import cmath
a=float(input())
b=float(input())
c=float(input())
dis = (b * b) - (4*a*c)
formula = (-b-dis**0.5)/(2*a)
formula1 = (-b+dis**0.5)/(2*a)
print(formula,formula1)
