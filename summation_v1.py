
# coding: utf-8

# **Write a function (in any language of the candidate’s choice) which returns True if the input integer array contains any two elements summing to 42. Return False otherwise**


def sum_42(x):
    """
    take into an iterable (an array of integers) and return True if any two elements summing to 42, return False
    otherwise.
    x is an array contains any number of integers: list, tuple, set
    
    Example:
    
        >>> sum_42([42]) 
        False
        >>> sum_42([1,5,8,9,20,19,40,21, 3, 33, 5])
        True
        >>> sum_42([21, 4, 21, 69, 21, 21])
        True
        >>> sum_42([46, 500, 188, 230])
        False
    """
    
    x = list(x)
    if len(x) < 2:
        return False
    if x.count(21) >= 2:
        return True
    else:
        for i in x:
            if i != 21 and 42-i in x:
                return True
    return False

if __name__ == '__main__':
    if (sum_42([42]) == False 
        and sum_42([1,5,8,9,20,19,40,21, 3, 33, 5]) == True 
        and sum_42([21, 4, 21, 69, 21, 21]) == True
        and sum_42([-2, 44]) == True
        and sum_42([46, 500, 188, 230]) == False
        ):
        print("Test for the sum_42 function was sucessful!")
    else:
        print("Test for the sum_42 function failed!")

