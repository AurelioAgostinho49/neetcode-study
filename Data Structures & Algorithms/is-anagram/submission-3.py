class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)
    
        if len(s_list) == len(t_list):
                
            for letter in t_list:
                if letter in s_list:
                    s_list.remove(letter)
                               
                else:
                    return False
        else:
        
            return False
    
        return True