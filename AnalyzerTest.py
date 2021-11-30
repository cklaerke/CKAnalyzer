import sys, os
import numpy as np
import matplotlib.pyplot as plt

# This is just a small test for running a script

def testing():
    """ Just a small funciton for running a test"""
    freq = 100.0
    x = np.linspace(0, 100, 1000)
    y = np.sin(2.0*np.pi*freq*x+np.pi/2.0)
    fig, ax = plt.subplots(figsize=(16,9))
    ax.plot(x,y, lw=1.8, ls='--')
    ax.grid(True)

    plt.show()


if __name__ == "__main__":
    testing()