import matplotlib.pyplot as plt
import numpy as np
import scipy
import scipy.integrate
from iteratedFunction import *
from pydmd import DMD, MrDMD, HODMD
from random import randrange

## initial condition
x_0 = 0.5

numdata = 100
randomdata = np.zeros((numdata,));
randomdata[0] = x_0;

for k in range(0, numdata - 1):

    if ((x_0 >= 0) and (x_0 < 0.25)):
        choice_prob = 1
    elif ((x_0 >= 0.25) and (x_0 < 0.75)):
        choice_prob = 2
    elif ((x_0 >= 0.75) and (x_0 <= 1.0)):
        choice_prob = 3

    x_0 = f(x_0, choice_prob)

    if x_0 > 1.0:
        x_0 = 0.0
    elif x_0 < 0.0:
        x_0 = 0.0
    else:
        pass

    randomdata[k + 1] = x_0

data = randomdata[1:len(randomdata)]

PPlot = False
if PPlot:

    fig = plt.figure()
    plt.plot(data)
    plt.show()

hodmd = HODMD(svd_rank=0, exact=True, opt=True, d=30).fit(data)

fig = plt.figure()

plt.plot(hodmd.dmd_timesteps, randomdata[0:len(randomdata) - 1], 'b*', label='Original function', linewidth=10.0)
plt.plot(hodmd.dmd_timesteps, hodmd.reconstructed_data[0].real, 'r*', label='IFS-DMD output', linewidth=10.0)
plt.xlabel("Iteration")
plt.legend()
plt.show()

fig = plt.figure()
plt.plot(hodmd.dmd_timesteps, abs(hodmd.reconstructed_data[0].real - randomdata[0:len(randomdata) - 1]) , 'b*', label='IFS - DMD error', linewidth=10.0)
plt.xlabel("Iteration")
plt.legend()
plt.show()






