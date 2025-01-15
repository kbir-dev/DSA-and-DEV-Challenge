class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        l1 = []
        for char in x:
            l1.append(char)
        if l1 == list(reversed(l1)):
            return True
        return False
    
    # x = str(x)
    #     return x == x[::-1]