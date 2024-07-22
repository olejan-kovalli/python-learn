"""
this module contains a function that can tell if the required power of 2 is in the provided list.
"""
def get_power_index(X, L):
    """
    Calculates whether the required power of 2 is in the provided list.
    X: power of 2
    L: list of values

    For example: 
        get_power_index(2, [1, 2, 4, 8, 16])
        at index 1

        get_power_index(10, [1, 2, 4, 8, 16])
        10 not found
    
    """
    if 2 ** X in L:
        print('at index', L.index(2 ** X))    
    else:
        print(X, 'not found')