'''
Leetcode problem: Two Sum
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

def twoSum(self, nums: List[int], target: int) -> List[int]:
    lst = []
    for i in range(len(nums)):
        val = target-nums[i]
        if val in nums:
            j = nums.index(val)
            if i!=j:
                lst.append(i)
                lst.append(j)
                return lst

