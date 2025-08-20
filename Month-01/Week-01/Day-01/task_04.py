'''Check if two lists are rotations of each other
Problem Statement:
Given two lists, list1 and list2, determine if list2 is a rotation of list1. A rotation means that list2 can be formed by taking some elements from the beginning of list1 and moving them to the end.

Example 1:
Input: list1 = [1, 2, 3, 4, 5], list2 = [3, 4, 5, 1, 2]
Output: True

Example 2:
Input: list1 = [1, 2, 3], list2 = [3, 2, 1]
Output: False

Constraints:

The lists can contain any type of elements.

The lists must have the same length to be considered rotations of each other.'''

def list_rotation(list1, list2):
    if len(list1) != len(list2):
        return False
    if not list1 and not list2:
        return True
    
    str1 = '$' + '$'.join(map(str, list1)) + '$'
    str2 = '$' + '$'.join(map(str, list2)) + '$'
    return str2 in (str1 + str1)

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 1, 2]
print(list_rotation(list1, list2))