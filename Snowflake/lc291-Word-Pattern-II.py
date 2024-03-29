class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        hashMap = {}
        def dfs(pattern, pIndex, s, sIndex, hashMap):
            if pIndex == len(pattern):
                return sIndex == len(s)
            curpattern = pattern[pIndex]
            if curpattern in hashMap:
                matchWord = hashMap[curpattern]
                if s[sIndex: sIndex + len(matchWord)] != matchWord:
                    return False
                return dfs(pattern, pIndex + 1, s, sIndex + len(matchWord), hashMap)
            res = False
            for endIndex in range(sIndex + 1, len(s) + 1):
                possibleWord = s[sIndex: endIndex]
                if possibleWord in hashMap.values():
                    continue
                hashMap[curpattern] = possibleWord
                if dfs(pattern, pIndex + 1, s, sIndex + len(possibleWord), hashMap):
                    return True
                # res = res or dfs(pattern, pIndex + 1, s, sIndex + len(possibleWord), hashMap)
                del hashMap[curpattern]
            return False
        return dfs(pattern, 0, s, 0, hashMap)