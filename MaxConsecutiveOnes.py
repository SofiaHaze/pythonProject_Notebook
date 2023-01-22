
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        cnt = 0
        max = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
                if i== len(nums) - 1:
                    if max < cnt:
                        max = cnt
            else:
                if max < cnt:
                    max = cnt
                cnt = 0

        return max
