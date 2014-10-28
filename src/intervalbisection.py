#Simple interval bisection method of root finding

#Performs interval bisection n times
#on the given function starting on the interval [a, b]
def interval_bisection(fn, a, b, n):
    for i in range(0, n):
        c = (a + b)/2.0
        res = fn(c)
        
        if res == 0:
            return c
        elif res < 0.0:
            a = c
        else:
            b = c
    return c 
