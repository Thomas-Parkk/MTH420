# standard_library.py
"""Python Essentials: The Standard Library.
<Name> Thomas Park
<Class> MTH 420
<Date> Friday, April 18th, 2025
"""

from math import sqrt
import calculator as bruh_calc
from itertools import combinations


# Problem 1
def prob1(L):
    """Return the minimum, maximum, and average of the entries of L
    (in that order, separated by a comma).
    """
    return min(L), max(L), sum(L) / len(L)
    #raise NotImplementedError("Problem 1 Incomplete")


# Problem 2
def prob2():
    """Determine which Python objects are mutable and which are immutable.
    Test integers, strings, lists, tuples, and sets. Print your results.
    """
    #for integers
    integer_test1 = 1
    integer_test2 = integer_test1
    integer_test2 +=1
    equal = integer_test1 == integer_test2
    if equal:
        print ("integer is mutable")
    else: 
        print ("integer is immutable")
    
    #for strings
    string_test1 = "bruh"
    string_test2 = string_test1
    string_test2 += "ayyo"
    equal = string_test1 == string_test2
    if equal:
        print ("string is mutable")
    else: 
        print ("string is immutable")
        
    #for lists
    list1 = [1, 2, 3]
    list2 = list1
    list2.append (4) 
    equal = list1 == list2
    if equal: 
        print ("list is mutable")
    else: 
        print ("list is immutable")
    
    #for tuples
    tup1 = (1,2,3)
    tup2 = tup1
    tup2 = tup1 + (4,)
    equal = tup1 == tup2
    if equal: 
        print ("tuple is mutable")
    else:
        print ("tuple is immutable")
        
    #for sets
    set1 = {1, 2, 3}
    set2 = set1
    set2.add (4)
    equal = set1 == set2
    if equal: 
        print ("set is mutable")
    else:
        print ("set is immutable")
    #raise NotImplementedError("Problem 2 Incomplete")


# Problem 3
def hypot(a, b):
    """Calculate and return the length of the hypotenuse of a right triangle.
    Do not use any functions other than sum(), product() and sqrt() that are
    imported from your 'calculator' module.

    Parameters:
        a: the length one of the sides of the triangle.
        b: the length the other non-hypotenuse side of the triangle.
    Returns:
        The length of the triangle's hypotenuse.
    """
    return bruh_calc.sqrt (bruh_calc.sum (bruh_calc.product (a,a), bruh_calc.product (b,b)))
    
    #raise NotImplementedError("Problem 3 Incomplete")


# Problem 4
A = {1, 2, 3}
def power_set(A):
    """Use itertools to compute the power set of A.

    Parameters:
        A (iterable): a str, list, set, tuple, or other iterable collection.

    Returns:
        (list(sets)): The power set of A as a list of sets.
    """
    from itertools import chain, combinations
    
    return (set (subset) for subset in chain.from_iterable (combinations (A, r) for r in range (len (A) + 1)))
    
    #raise NotImplementedError("Problem 4 Incomplete")


# Problem 5: Implement shut the box.
def shut_the_box(player, timelimit):
    """Play a single game of shut the box."""
    #raise NotImplementedError("Problem 5 Incomplete")

if __name__ == "__main__":

    L = [1, 2, 3, 4, 5]
    print (prob1 (L))
    
    prob2 ()
    
    a = 3
    b = 4
    print (hypot (a,b))
    
    print(list(power_set (A)))