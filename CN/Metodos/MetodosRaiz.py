import math

def bissec(f,a,b,tol):
    error = math.inf
    status = 0
    n = 0

    if (f(a)*f(b) > 0): return math.nan, n, status

    elif (f(a)*f(b) == 0):
        if (f(a) == 0): return a, n, status

        else: return b, n, status

    while error > tol:
        c = (a+b)/2

        if (f(a)*f(c) < 0):
            b = c

        elif (f(b)*f(c)<0):
            a = c

        else:
            n += 1
            break

        error = abs(f(c))
        n += 1

    status = 1
    return c, n, status


def falsepos(f,a,b,tol,maxiter):
    status = 0
    c=(a*f(b)-b*f(a))/(f(b)-f(a))
    fc = f(c)
    n = 1

    if (f(a)*f(b) > 0): return status, n, c

    elif (f(a)*f(b) == 0):
        if (f(a) == 0):
            status = 2
            return status, n, a
        else:
            status = 2
            return status, n, b

    while ((abs(fc) > tol) and (n < maxiter)):
        if (f(a)*fc > 0):
            a = c
        else:
            b = c

        c=(a*f(b)-b*f(a))/(f(b)-f(a))
        fc = f(c)
        n += 1

    status = 1
    return status, n, c


def newton(f,fd,x0,tol,maxiter):
    status = 0
    n = 0
    xs = x0

    while ((abs(f(x0)) > tol) and (n < maxiter)):
        if fd(x0) == 0 : 
            status = 2
            return x0, n, status

        x0 = x0 - (f(x0)/fd(x0))
        n += 1

    if ((n == maxiter) and (xs == x0)):
        status = 2
        return x0, n, status

    status = 1
    return x0, n, status


def sec(f,x1,x0,tol,maxiter):
    status = 0
    n = 0
    error = math.inf


    while ((error > tol) and (n < maxiter)):
        if (f(x1) == f(x0)):
            status = 2
            return c, n, status
        
        c = x1 - f(x1)*((x0 - x1)/(f(x0) - f(x1)))
        error = abs(f(c))
        x0 = x1
        x1 = c
        n += 1

    status = 1
    return c, n, status


#secante
""" 
def f(x)  : return x**3 - 6.126*x**2
x0 = 8.126
x1 = 7.126
tol = 1E-10
maxiter = 20
saida = sec(f,x1,x0,tol,maxiter)
print("Raiz aproximada = %.9f | Iterações = %d | Status = %d"%(saida[0],saida[1],saida[2]))
print("%.9f"%f(saida[0]))
 """

#newton

def f(x)  : return   math.sin(x)
def fd(x) : return   math.cos(x)
x0 = 10.360972571539
tol = 1E-14
maxiter = 3
saida = newton(f,fd,x0,tol,maxiter)
print("Raiz aproximada = %.9f | Iterações = %d | Status = %d"%(saida[0],saida[1],saida[2]))
print(f(saida[0]))


#bissecao
"""
def f(x): return x**5+x**4-3.3
a=1.1173
b=1.1174
tol=10**(-5)
saida=bissec(f,a,b,tol)
print('f(a)=',f(a))
print('f(b)=',f(b))
print(saida)
"""

#falsa posicao
"""
def f(x): return x**5+x**4-3.3
a=1.1173 
b=1.1174
tol=10**(-15)
maxiter=100
saida=falsepos(f,a,b,tol,maxiter)
print(saida[0], saida[1], saida[2])
"""