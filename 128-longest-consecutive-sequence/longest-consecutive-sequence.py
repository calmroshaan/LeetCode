class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        answer = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                answer = max(answer, y-x)
        return answer