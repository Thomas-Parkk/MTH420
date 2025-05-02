# numpy_intro.py
"""Python Essentials: Intro to NumPy.
<Name> Thomas Park
<Class> MTH 420
<Date> Tuesday, April 22nd, 2025
"""

import numpy as np


def prob1():
    """ Define the matrices A and B as arrays. Return the matrix product AB. """
    A = np.array ([[3, -1, 4], [1, 5, -9]])
    B = np.array ([[2, 6, -5, 3], [5, -8, 9, 7], [9, -3, -2, -3]])
    return A @ B

    raise NotImplementedError("Problem 1 Incomplete")


def prob2():
    """ Define the matrix A as an array. Return the matrix -A^3 + 9A^2 - 15A. """
    A = np.array ([[3, 1, 4], [1, 5, 9], [-5, 3, 1]])
    A_2 = A @ A
    A_3 = A @ A @ A
    return -A_3 + 9 * A_2 - 15 * A

    raise NotImplementedError("Problem 2 Incomplete")


def prob3():
    """ Define the matrices A and B as arrays using the functions presented in
    this section of the manual (not np.array()). Calculate the matrix product ABA,
    change its data type to np.int64, and return it.
    """
    A = np.triu(np.ones((7,7)))
    B_lower = np.tril(np.full((7,7), -1))
    B_upper = np.triu(np.full((7,7), 5), 1)
    B = B_lower + B_upper
    matrix_product = A @ B @ A
    return print (matrix_product.astype (np.int64))
    raise NotImplementedError("Problem 3 Incomplete")

A = np.array([-3,-1,3])
def prob4(A):
    """ Make a copy of 'A' and use fancy indexing to set all negative entries of
    the copy to 0. Return the resulting array.

    Example:
        >>> A = np.array([-3,-1,3])
        >>> prob4(A)
        array([0, 0, 3])
    """
   # A = np.array([-3,-1,3])
    A_copy = np.copy (A)
    mask = A_copy < 0
    A_copy [mask] = 0
    return A_copy
    raise NotImplementedError("Problem 4 Incomplete")


def prob5():
    """ Define the matrices A, B, and C as arrays. Use NumPy's stacking functions
    to create and return the block matrix:
                                | 0 A^T I |
                                | A  0  0 |
                                | B  0  C |
    where I is the 3x3 identity matrix and each 0 is a matrix of all zeros
    of the appropriate size.
    """
    A = np.array ([[0, 2, 4], [1, 3, 5]])
    B = np.tril(np.full((3,3), 3))
    C = np.diag(np.full(3,-2))
    I = np.diag(np.full(3,1))
    A_T = np.transpose (A)
    Zero_1 = np.full((3,3), 0)
    Zero_2 = np.full((2,2), 0)
    Zero_3 = np.full((3,2), 0)
    Zero_3_T = np.transpose (Zero_3)
    
    Stack_1 = np.hstack ((Zero_1, A_T, I))
    Stack_2 = np.hstack ((A, Zero_2, Zero_3_T))
    Stack_3 = np.hstack ((B, Zero_3, C))
    
    Big_Stack = np.vstack ((Stack_1, Stack_2, Stack_3))
    
    return Big_Stack
    raise NotImplementedError("Problem 5 Incomplete")


def prob6(A):
    """ Divide each row of 'A' by the row sum and return the resulting array.
    Use array broadcasting and the axis argument instead of a loop.

    Example:
        >>> A = np.array([[1,1,0],[0,1,0],[1,1,1]])
        >>> prob6(A)
        array([[ 0.5       ,  0.5       ,  0.        ],
               [ 0.        ,  1.        ,  0.        ],
               [ 0.33333333,  0.33333333,  0.33333333]])
    """
    A = np.array([[1,1,0],[0,1,0],[1,1,1]])
    for row in A
        row_sum = 0
        for A in range (0, len(A)):
            A_copy.append (A / total)
    return A_copy

    raise NotImplementedError("Problem 6 Incomplete")


#def prob7():
    """ Given the array stored in grid.npy, return the greatest product of four
    adjacent numbers in the same direction (up, down, left, right, or
    diagonally) in the grid. Use slicing, as specified in the manual.
    """
    #raise NotImplementedError("Problem 7 Incomplete")

if __name__ == "__main__":
    print (prob1())
    
    print (prob2())
    
    print (prob3())
    
    print (prob4(A))
    
    print (prob5())
    
    print (prob6(A))
    