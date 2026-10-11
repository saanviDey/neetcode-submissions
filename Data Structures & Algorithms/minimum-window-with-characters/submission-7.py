class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT = {}
        window = {}

        for i in t:
            countT[i] = 1 + countT.get(i, 0)
        
        have = 0
        # countT and not t because it gives length of unique chars in string t
        need = len(countT)

        l = 0
        res = [-1, -1]
        resLen = float("infinity") # greatest positive value
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need:
                # update result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                # pop from left of our window
                window[s[l]] = window[s[l]] - 1
                if s[l] in t and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        if resLen != float("infinity"):
            return s[l:r+1]
        else:
            return ""



        