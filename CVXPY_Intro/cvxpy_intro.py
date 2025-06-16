# cvxpy_intro.py
"""Volume 2: Intro to CVXPY.
<Name> Thomas Park
<Class> MTH 420
<Date> Sunday, June 16th 2025
"""

import numpy as np
import cvxpy as cp

def prob1():
    """Solve the following convex optimization problem:

    minimize        2x + y + 3z
    subject to      x  + 2y         <= 3
                         y   - 4z   <= 1
                    2x + 10y + 3z   >= 12
                    x               >= 0
                          y         >= 0
                                z   >= 0

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    x_con = cp.Variable (3, nonneg = True)
    cost = np.array ([2, 1, 3])
    objective = cp.Minimize (cost.T @ x_con)


    constraints = [x_con[0] + 2 * x_con[1] <= 3, 
                   x_con[1] - 4 * x_con[2] <= 1,
                   2 * x_con[0] + 10 * x_con[1] + 3 * x_con[2] >= 12]
    goal = cp.Problem (objective, constraints)
    optimal_value_y = problem.solve()
    
    return x_con.value, optimal_value_y

    # raise NotImplementedError("Problem 1 Incomplete")


# Problem 2
def l1Min(A, b):
    """Calculate the solution to the optimization problem

        minimize    ||x||_1
        subject to  Ax = b

    Parameters:
        A ((m,n) ndarray)
        b ((m, ) ndarray)

    Returns:
        The optimizer x (ndarray)
        The optimal value (float)
    """
    m, n = A. shape
    x_variable = cp.Variable (n)
    objective = cp.Minimize (cp.norm (x_variable,1) )
    constraint = [A @ x_variable == b]
    
    goal = cp.Problem (objective, constraint)
    optimal_value_y = problem.solve()
    
    return x_variable.value, optimal_value_y
    # raise NotImplementedError("Problem 2 Incomplete")


# Problem 3
def prob3():
    """Solve the transportation problem by converting the last equality constraint
    into inequality constraints.

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    x_variable = cp.Variable (6, nonneg = True)
    cost = np.array ([4, 7, 6, 8, 8, 9])
    objective = cp.Minimize (cost.T @ x_variable)
    constraints = [x_variable[0] + x_variable[1] <= 7, 
                   x_variable[2] + x_variable[3] <= 2, 
                   x_variable[4] + x_variable[5] <= 4, 
                   x_variable[0] + x_variable[2] + x_variable[4] == 5,
                   x_variable[1] + x_variable[3] + x_variable[5] == 8]
    goal = cp.Problem (objective, constraints)
    optimal_value_y = problem.solve()
    
    return x_variable.value, optimal_value_y   
    #raise NotImplementedError("Problem 3 Incomplete")


# Problem 4
def prob4():
    """Find the minimizer and minimum of

    g(x,y,z) = (3/2)x^2 + 2xy + xz + 2y^2 + 2yz + (3/2)z^2 + 3x + z

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    
    
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5
def prob5(A, b):
    """Calculate the solution to the optimization problem
        minimize    ||Ax - b||_2
        subject to  ||x||_1 == 1
                    x >= 0
    Parameters:
        A ((m,n), ndarray)
        b ((m,), ndarray)
        
    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def prob6():
    """Solve the college student food problem. Read the data in the file 
    food.npy to create a convex optimization problem. The first column is 
    the price, second is the number of servings, and the rest contain
    nutritional information. Use cvxpy to find the minimizer and primal 
    objective.
    
    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """	 
    raise NotImplementedError("Problem 6 Incomplete")
    
if __name__ == "__main__":
    prob1 ()
    prob3 ()
    
    