from numericalmethods.romberg import *

fn = lambda x : exp(-x)
a = 3
b = 10

print(romberg(a, b, fn, 4))

a = 0
b = 1
fn2 = lambda x : 1 / (1 + x)
print(romberg(a, b, fn2, 3))
