class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        j = 1
        for i in range(1,n):
                if nums[i-1] != nums[i]:
                    nums[j] = nums[i]
                    j+=1
        return j