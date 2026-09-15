class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        max_length = 0 
        left = 0
        for right in range(len(s)):
            while s[right] in sett:
                sett.remove(s[left])
                left+=1
            sett.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length