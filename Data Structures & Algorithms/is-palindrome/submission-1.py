class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = re.sub(r"[^a-z0-9]", "", s.lower())
        l = 0 
        r = len(result) - 1 
        
        while l <= r:
            if result[l] != result[r]:
                return False
            l +=1
            r -=1

        return True