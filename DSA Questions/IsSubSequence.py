class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l1 = [] 
        i = 0
        j = 0
        
        while i < len(s) and j < len(t):
            if s[i] == t[j]:  
                l1.append(t[j]) 
                i += 1  
            j += 1 
        
        l1 = "".join(l1)
        
        return s == l1