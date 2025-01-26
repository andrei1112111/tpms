import random
import matplotlib.pyplot as plt
from math import pi

from numba import njit

square_a = 2
square_s = square_a * square_a
circle_radius = square_a / 2

in_circle = 0
repeat = 100000000

point_n = 10000


@njit(parallel=True)
def monte_carlo_pi(nsamples):
    nsample = []
    prob = []
    acc = 0
    for i in range(1, nsamples):
        x = random.uniform(-circle_radius, circle_radius)
        y = random.uniform(-circle_radius, circle_radius)

        if x ** 2 + y ** 2 < circle_radius:
            acc += 1

        if i % point_n == 0:
            nsample.append(i)
            prob.append(square_s * acc / i)
            # print((i, (square_s * acc / nsamples)))

    print(prob[-1])
    return nsample, prob

"""
in_circle     s circle
---------  =  --------
  repeat      s square
  
in_circle * s square = repeat * s circle

in_circle * s square
-------------------- = s circle
       repeat
"""


x = []
y = []

for i in range(point_n):
    x.append(i*repeat/point_n)
    y.append(pi)
plt.plot(x, y)

plt.plot(*monte_carlo_pi(repeat))

plt.xlabel("nsample")
plt.ylabel("pi")
plt.show()
