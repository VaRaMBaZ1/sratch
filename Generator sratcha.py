from numba import prange
f1 = open("sratch.txt", 'w')

for i in prange(0, 1000000):
    for a in prange(0, 1000000):
        for x in prange(0, 1000000):
            for y in prange(0, 1000000):
                f1.write(str(i) + str(a) + str(x) + str(y) + "\n")

