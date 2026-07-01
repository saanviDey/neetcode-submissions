class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            count = [0] * 26  # key which is frequency of characters
            for c in s:
                count[ord(c) - ord('a')] += 1
            result[tuple(count)].append(s)  # adding the string based on the key
        return list(result.values())

        