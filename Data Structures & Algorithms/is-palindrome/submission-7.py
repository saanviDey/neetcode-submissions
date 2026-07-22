class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = ''.join([char for char in s.lower() if char.isalnum()])
        print(clean_text)

        for i in range(len(clean_text)//2):
            if clean_text[i] != clean_text[len(clean_text) - 1 - i]:
                return False
        
        return True
        

        