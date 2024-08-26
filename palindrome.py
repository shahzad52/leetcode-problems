class Solution(object):
    def isPalindrome(self, x):
        num = x
        res = str(num)
        y = res [::-1]
        if res == y:
            return True
        return False
        """
        :type x: int
        :rtype: bool
        """
        
