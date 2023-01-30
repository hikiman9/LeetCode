class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []

        for i in s:
            if i.isalnum():
                strs.append(i.lower())
        
        while len(strs) > 1:
            if strs.pop() != strs.pop(0):
                return False
        
        return True