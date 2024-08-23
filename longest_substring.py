'''Given a string s, find the length of the longest 
substring
 without repeating characters. '''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        set1 = set()
        lenght = 0
        result = 0
        for right in range (len(s)):
            while s[right] in set1:
                set1.remove(s[left])
                left += 1
            set1.add(s[right])
            result = max(result,right-left+1)
        return result
        
