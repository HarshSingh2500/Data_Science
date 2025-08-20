'''Find the second largest element in a list
Problem Statement:
Given a list of integers, find the second largest element in the list. The list may contain duplicate elements. If there is no second largest element (e.g., the list has fewer than two unique elements), return None.

Example 1:
Input: nums = [3, 1, 4, 1, 5, 9, 2, 6]
Output: 6

Example 2:
Input: nums = [5, 5, 5]
Output: None

Constraints:

The list will contain only integers.

The list can be empty.'''


# Approach 1: Make list a set then return second largest element
# def second_largest(li):
#     list_set = set(li)
#     unique_list = list(list_set)
#     return unique_list[-2]

# Approach 2: Iterating the list once and keeping track of the largest and second largest element
def second_largest(li):
    largest_element = -1
    second_largest_element = -1
    for i in li:
        if i > largest_element:
            second_largest_element = largest_element
            largest_element = i
        elif i > second_largest_element and i < largest_element:
            second_largest_element = i
    
    return second_largest_element

# li = [3, 1, 4, 1, 5, 9, 2, 6]
# li = [5, 5, 5]
# li = []
li = [2]

n = len(li)
if len(li) < 1:
    print("list is empty")
else:
    list_sum = sum(li)
    list_product = li[0]*n
    if list_sum == list_product:
        print("None")
    else:
        print(second_largest(li))