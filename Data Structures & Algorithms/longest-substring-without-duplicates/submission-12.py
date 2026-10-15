class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # index r as right boundary and l as left bounary
        # use hash set to check if character is present
        # if we see character at index r, shrink window by l++ 
        # remove characters from hash set as l pointer moves
        # update result with length of current window (r - l + 1)

        seen = set()
        l = 0
        length = 0
        for r in range(len(s)):
       
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
    
            seen.add(s[r])
            
            length = max(length, r-l+1)
        
        return length