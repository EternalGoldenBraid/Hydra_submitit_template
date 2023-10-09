import matplotlib.pyplot as plt
import numpy as np

def plot_gaussian():

    fig, ax = plt.subplots()

    x = np.linspace(-1,1,100)
    ax.plot(x, np.exp(x)/np.sqrt(2*np.pi))
    
    return fig
    