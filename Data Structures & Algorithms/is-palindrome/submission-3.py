class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        filtrada = "".join(char.lower() for char in s if char.isalnum())
        inverted = ""

        for char in filtrada:
            inverted = char + inverted

        if filtrada == inverted:
            return True

        return False