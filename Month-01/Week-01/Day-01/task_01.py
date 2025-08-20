'''Reverse a list without using reverse()
Problem Statement:
Given a list of elements, write a function to reverse the order of the elements in the list. You are not allowed to use the built-in list.reverse() method or slicing [::-1].

Example:
Input: nums = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]

Constraints:

The input list can contain any type of elements (integers, strings, etc.).

The reversal should be done in-place, modifying the original list.'''

li = [1, 2, 3, 4, 5]
n = len(li)
for i in range(n//2):
    li[i], li[n-i-1] = li[n-i-1], li[i]
print(li)