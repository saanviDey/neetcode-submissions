class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # use hashmap to count frequency
        freq_s = {}
        freq_t = {}

        for c in s:
            freq_s[c] = 1 + freq_s.get(c, 0)

        for c in t:
            freq_t[c] = 1 + freq_t.get(c, 0)
        
        return freq_s == freq_t