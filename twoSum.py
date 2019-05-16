
"""

If nums is a list of numbers and target is a int which is a cummilative of two integers in nums find the indices of the numbers 
that equal target - Leetcode problem 1

nums = [2,5,6,7]
target = 7

create an empty Dictionary that can store the number and index of the difference between target and the number , when the dictionary has the difference it will be returned  
"""

def twoSum(nums, target):
dictionary = {}
for index,number in enumerate(nums):
     if target - number in dictionary:
          return dictionary[target-number], index
     dictionary[number] = index
