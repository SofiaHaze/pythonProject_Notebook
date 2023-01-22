

class Solution:
    def twoSum(self, nums, target):
        """
        def twoSum(self, nums: List[int], target: int) -> List[int]:
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        break_check = False
        for i in range(0, len(nums)+1):
            for j in range(i+1, len(nums)):
                #print(f'{i,j}')
                if (nums[i]+nums[j])==target:
                    break_check = True
                    return [i, j]
                    break
            if break_check:
                break