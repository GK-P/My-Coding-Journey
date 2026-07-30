class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_list = {}

        for c in s:
            if c in count_list:
                count_list[c] += 1
            else:
                count_list[c] = 1

        for c in t:
            if c not in count_list:
                return False
            
            count_list[c] -= 1

            if count_list[c] < 0:
                return False
    
        return True
              

        
