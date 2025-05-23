# matplotlib_intro.py
"""Python Essentials: Intro to Matplotlib.
<Name> Thomas Park
<Class> MTH 420 
<Date> Friday, May 2nd 2025
"""

import numpy as np
from matplotlib import pyplot as plt

# Problem 1
def var_of_means(n):
    """ Create an (n x n) array of values randomly sampled from the standard
    normal distribution. Compute the mean of each row of the array. Return the
    variance of these means.

    Parameters:
        n (int): The number of rows and columns in the matrix.
        
    Returns:
        (float) The variance of the means of each row.
    """
    A = np.random.normal(size=(n, n)) 
    
    mean_row = np.mean (A, axis=1)
    
    variance = np.var (mean_row)
    return variance
    #raise NotImplementedError("Problem 1 Incomplete")

def prob1():
    """ Create an array of the results of var_of_means() with inputs
    n = 100, 200, ..., 1000. Plot and show the resulting array.
    """
    #raise NotImplementedError("Problem 1 Incomplete")
    array_y = []
    array_x = []
    for i in range(100, 1100, 100):
        # np.append(array_y, var_of_means(i))
        # np.append (array_x, i)
        array_y.append(var_of_means(i))
        array_x.append(i)
    
    plt.plot (array_x,array_y)
    plt.title("Array Plot")
    plt.xlabel("n Values")
    plt.ylabel("Variance of Means")
    plt.show()


# Problem 2
def prob2():
    """ Plot the functions sin(x), cos(x), and arctan(x) on the domain
    [-2pi, 2pi]. Make sure the domain is refined enough to produce a figure
    with good resolution.
    """
    
    x = np.linspace (-2 * np.pi, 2 * np.pi, 10000)
    plt.plot(x, np.sin(x), label ="sin(x)")
    plt.plot(x, np.cos(x), label ="cos(x)")
    plt.plot(x, np.arctan(x), label ="arctan(x)")
    plt.legend()
    plt.grid(True)
    plt.show()
    

# Problem 3
def prob3():
    """ Plot the curve f(x) = 1/(x-1) on the domain [-2,6].
        1. Split the domain so that the curve looks discontinuous.
        2. Plot both curves with a thick, dashed magenta line.
        3. Set the range of the x-axis to [-2,6] and the range of the
           y-axis to [-6,6].
    """
    first_x = np.linspace (-2, 0.9999, 400)
    second_x = np.linspace (1.0001, 6, 400)
    
    plt.plot (first_x, 1/ (first_x - 1), 'm--', lw=3, label ="f(x) = 1/(x-1)")
    plt.plot (second_x,1/ (second_x - 1), 'm--', lw=3)
    
    plt.xlim (-2,6)
    plt.ylim (-6,6)
    plt.title ("Plot of f(x) = 1/(x-1) on the Domain [-2,6]")
    plt.xlabel ("x")
    plt.ylabel ("f(x)")
    plt.show ()
    #raise NotImplementedError("Problem 3 Incomplete")


# Problem 4
def prob4():
    """ Plot the functions sin(x), sin(2x), 2sin(x), and 2sin(2x) on the
    domain [0, 2pi], each in a separate subplot of a single figure.
        1. Arrange the plots in a 2 x 2 grid of subplots.
        2. Set the limits of each subplot to [0, 2pi]x[-2, 2].
        3. Give each subplot an appropriate title.
        4. Give the overall figure a title.
        5. Use the following line colors and styles.
              sin(x): green solid line.
             sin(2x): red dashed line.
             2sin(x): blue dashed line.
            2sin(2x): magenta dotted line.
    """
    
    #raise NotImplementedError("Problem 4 Incomplete")


# Problem 5
#def prob5():
    """ Visualize the data in FARS.npy. Use np.load() to load the data, then
    create a single figure with two subplots:
        1. A scatter plot of longitudes against latitudes. Because of the
            large number of data points, use black pixel markers (use "k,"
            as the third argument to plt.plot()). Label both axes.
        2. A histogram of the hours of the day, with one bin per hour.
            Label and set the limits of the x-axis.
    """
    #raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def prob6():
    """ Plot the function g(x,y) = sin(x)sin(y)/xy on the domain
    [-2pi, 2pi]x[-2pi, 2pi].
        1. Create 2 subplots: one with a heat map of g, and one with a contour
            map of g. Choose an appropriate number of level curves, or specify
            the curves yourself.
        2. Set the limits of each subplot to [-2pi, 2pi]x[-2pi, 2pi].
        3. Choose a non-default color scheme.
        4. Include a color scale bar for each subplot.
    """
    raise NotImplementedError("Problem 6 Incomplete")
    
    
if __name__ == "__main__":
    
    prob2()
    prob3 ()
    prob4()
