import os
import math
import logging
import numpy as np

def sigmoid(x):
    try:
        if x < 0:
            return 1 - 1 / (1 + math.exp(x))
        return 1 / (1 + math.exp(-x))
    except Exception as err:
        print("Error in sigmoid: " + err)

def get_state(data, t, n_days):
    # returns a n_day state for a given time step t
    
    d = t - n_days + 1
    block = data[d: t + 1] if d >= 0 else -d * [data[0]] + data[0: t + 1]  # pad with intial amount in the starting.
    res = []
    # normalising the data
    for i in range(n_days - 1):
        res.append(sigmoid(block[i + 1] - block[i]))
    return np.array([res])

    