from mat import Mat
from vec import Vec
from GF2 import one

A = Mat(({0,1,2}, {0,1,2}), {(1,1):4, (0,0):0, (1,2):1, (1,0):5, (0,1):3, (0,2):2})
B = Mat(({0,1,2}, {0,1,2}), {(1,0):5, (2,1):3, (1,1):2, (2,0):0, (0,0):1, (0,1):4})
print(A*B == Mat(({0,1,2}, {0,1,2}), {(0,0):15, (0,1):12, (1,0):25, (1,1):31}))
#True