'''Flatten a nested list [[1,2],[3,4]] → [1,2,3,4]
Problem Statement:
Given a nested list of integers, where each sublist contains integers, write a function to flatten it into a single, one-dimensional list.

Example 1:
Input: nested_list = [[1, 2], [3, 4], [5]]
Output: [1, 2, 3, 4, 5]

Example 2:
Input: nested_list = [[], [1, 2], []]
Output: [1, 2]

Constraints:

The input is a list of lists.

Each sublist contains only integers.

The sublists can be empty.'''

def flatten_list(li):
    new_list = []
    for sub_li in li:
        if len(sub_li) < 1:
            continue
        else:
            for i in sub_li:
                new_list.append(i)
    return new_list

# nums = [[1, 2], [3, 4], [5]]
nums = [[], [1, 2], []]
print(flatten_list(nums))