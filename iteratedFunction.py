import numpy as np
from random import randrange


## functions
def f(x_k, choice):

    if choice == 1:
        out = 4 * x_k * (1 - x_k) / 5.0

    elif choice == 2:
        out = 14 * x_k * (1 - x_k) / 5.0

    elif choice == 3:
        out = 19 * x_k * (1 - x_k) / 5.0

    else:
        "more than 4"

    return out

if __name__ == "__main__":

    x_0 = 0.5

    numdata = 100
    randomdata = np.zeros((numdata,));
    randomdata[0] = x_0;

    #choice_prob = [0.25, 0.50, 0.25]
    for k in range(0, numdata - 1):

        if ((x_0 >= 0) and (x_0 < 0.25)):
            choice_prob = 1
        elif ((x_0 >= 0.25) and (x_0 < 0.75)):
            choice_prob = 2
        elif ((x_0 >= 0.75) and (x_0 <= 1.0)):
            choice_prob = 3


        x_kplusone = f(x_0, choice_prob)
        x_0 = x_kplusone

        if x_0 > 1.0:
            x_0 = 0.0
        elif x_0 < 0.0:
            x_0 = 0.0
        else:
            pass

        randomdata[k+1] = x_0

    np.save('data.npy', randomdata)


