class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = {}
        result = []
        for i in range(len(strs)):
            charCount = [0]*26
            for char in strs[i]:
                charCount[ord(char) - 97] += 1
            
            key = tuple(charCount)
            if key in groupings:
                groupings[key].append(strs[i])
            else:
                groupings[key] = [strs[i]]

        for grouping in groupings:
            result.append(groupings[grouping])

        return result

