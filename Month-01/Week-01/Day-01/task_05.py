'''Function that returns (min, max, mean) of a tuple
Problem Statement:
Given a tuple of numbers, write a function that calculates and returns a new tuple containing the minimum value, maximum value, and the mean (average) of the elements in the input tuple.

Example:
Input: t = (1, 2, 3, 4, 5)
Output: (1, 5, 3.0)

Constraints:

The input tuple will contain only numerical elements (integers or floats).

The input tuple can be empty. In this case, your function should return (None, None, None).'''

def arithmetic_operation(t):
    if not t:
        new_t = ('none', 'none', 'none')
        return new_t
    max_element = max(t)
    min_element = min(t)
    mean = sum(t)/len(t)
     
    return  (max_element, min_element, mean)

# t = (1, 2, 3, 4, 5)
t = ()
print(arithmetic_operation(t))