class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n_zeroes = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                n_zeroes += 1
            elif n_zeroes > 0:
                t = nums[i]
                nums[i] = 0
                nums[i - n_zeroes] = t
        