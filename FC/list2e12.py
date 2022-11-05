import random

cir = 0
sqr = 0

while sqr != 4*(10**7):
    x = random.random()*2
    y = random.random()*2
    sqr += 1
    if ((x**2)+(y**2)) <= 4:
        cir += 1

pi = 4*(cir/sqr)
print(pi)
