# python_intro.py
"""Python Essentials: Introduction to Python.
<Name> Thomas Park
<Class> MTH420
<Date> Tuwsday, April 8th, 2025
"""


# Problem 1 (write code below)


# Problem 2
def sphere_volume(r):
    """ Return the volume of the sphere of radius 'r'.
    Use 3.14159 for pi in your computation.
    """
    pi = 3.14159
    return (4 / 3) * pi * (r ** 3)
    #raise NotImplementedError("Problem 2 Incomplete")


# Problem 3
def isolate(a, b, c, d, e):
    """ Print the arguments separated by spaces, but print 5 spaces on either
    side of b.
    """
    print (a, b, c, sep="     ", end = " ")
    print (d, e)
    #raise NotImplementedError("Problem 3 Incomplete")


# Problem 4
def first_half(my_string):
    """ Return the first half of the string 'my_string'. Exclude the
    middle character if there are an odd number of characters.

    Examples:
        >>> first_half("python")
        'pyt'
        >>> first_half("ipython")
        'ipy'
    """
    middle_word = len(my_string)//2
    return my_string[:middle_word]
    #raise NotImplementedError("Problem 4 Incomplete")

def backward(my_string):
    """ Return the reverse of the string 'my_string'.

    Examples:
        >>> backward("python")
        'nohtyp'
        >>> backward("ipython")
        'nohtypi'
    """
    return my_string[::-1]
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5
def list_ops():
    """ Define a list with the entries "bear", "ant", "cat", and "dog".
    Perform the following operations on the list:
        - Append "eagle".
        - Replace the entry at index 2 with "fox".
        - Remove (or pop) the entry at index 1.
        - Sort the list in reverse alphabetical order.
        - Replace "eagle" with "hawk".
        - Add the string "hunter" to the last entry in the list.
    Return the resulting list.

    Examples:
        >>> list_ops()
        ['fox', 'hawk', 'dog', 'bearhunter']
    """
    l_list = ["bear", "ant", "cat", "dog"]
    l_list.append ("eagle")
    l_list[2] = ("fox") 
    l_list.pop (1)
    l_list.sort (reverse = True)
    eagle_list = l_list.index ("eagle")
    l_list[eagle_list] = ("hawk")
    l_list[-1] += "hunter"
    return l_list
    #raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def pig_latin(word):
    """ Translate the string 'word' into Pig Latin, and return the new word.

    Examples:
        >>> pig_latin("apple")
        'applehay'
        >>> pig_latin("banana")
        'ananabay'
    """
    vowels = {"a", "e", "i", "o", "u"}
    if word[0] in vowels:
        return word + "hay"
    else: 
        return word [1:] + word [0] + "ay"
    #raise NotImplementedError("Problem 6 Incomplete")


# Problem 7
def palindrome():
    """ Find and retun the largest panindromic number made from the product
    of two 3-digit numbers.
    """
    pdrome = 0
    for x in range (100,1000):
        for y in range (100,1000):
            product = x * y
            if str (product) == str (product) [::-1]:
                if product > pdrome:
                    pdrome = product
    return pdrome
    #raise NotImplementedError("Problem 7 Incomplete")

# Problem 8
def alt_harmonic(n):
    """ Return the partial sum of the first n terms of the alternating
    harmonic series, which approximates ln(2).
    """
    return sum((-1) ** (b+1) / b for b in range (1, n+1))
    
    #raise NotImplementedError("Problem 8 Incomplete")

if __name__ == "__main__":
    print("Hello, world!")
    
    r=3
    print(sphere_volume(r))
    
    print (isolate ('a', 'b', 'c', 'd', 'e'))
    
    my_string="python"
    
    print (first_half(my_string))
    print (backward(my_string))
    
    print (list_ops())
    
    word = "bruh"
    print (pig_latin(word))
    
    print (palindrome())
    
    print (alt_harmonic(500000))