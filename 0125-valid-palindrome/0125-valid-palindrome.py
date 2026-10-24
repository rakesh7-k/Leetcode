class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss="".join(char.lower() for char in s if char.isalnum())
        if ss==ss[::-1]:
            return True
        return False