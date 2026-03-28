1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        h, n = len(haystack), len(needle)
4        
5        for i in range(h - n + 1):
6            if haystack[i : i + n] == needle:
7                return i
8                
9        return -1