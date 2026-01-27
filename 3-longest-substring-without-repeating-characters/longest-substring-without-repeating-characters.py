class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        left = 0
        bucket = set()
        for right in range(len(s)):
            while s[right] in bucket:
                bucket.remove(s[left])
                left += 1
            bucket.add(s[right])
            answer = max(answer, right - left + 1)
        return answer
