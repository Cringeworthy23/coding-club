# install numpy, explain that random is a preinstalled module
import random
import numpy as np

def stddev(): 
    mean = 5
    std = 2
    value = np.random.normal(mean, std, 100)
    # normal can be substituted for binomial, poisson, etc.
    for i in range(10):
        print(value[i])

def random_numbers():
    for i in range(10):
        numbers = random.randint(1, 10)
        print(numbers)
