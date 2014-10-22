#Romberg Integration

from math import exp

#Takes a start and end real values to mark the interval,
#a real valued function to integrate and n the depth to go to
#larger n is higher accuracy is
def romberg(start_interval, end_interval, fn, n):
    values = {} #Stores romberg values
    hk = lambda k : (end_interval - start_interval) / 2**k
    fki = lambda k, i : fn(start_interval + (hk(k) * i))

    values[(0,0)] = (hk(0)/2)*(fki(0,0) + fki(0,1)) #R 0,0

    for k in range(1, n + 1): #R 1,0 to #R n,0
        lhs = (1/2) * values[(k - 1, 0)]
        rhs = hk(k) * sum(fki(k, 2*i - 1) for i in range (1, 1 + (2**(k-1))))
        values[(k, 0)] = lhs + rhs

    for k in range(1, n + 1):
        for m in range(1, k + 1):
            val = ((4**m * (values[(k, m - 1)])) - (values[(k - 1, m - 1)]))/ (4**m - 1)
            values[(k, m)] = val

    return values[(n, n)]


fn = lambda x : exp(-x)
a = 3
b = 10

print(romberg(a, b, fn, 4))

a = 0
b = 1
fn2 = lambda x : 1 / (1 + x)
print(romberg(a, b, fn2, 3))
