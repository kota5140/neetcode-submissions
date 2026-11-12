class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ans = []
        l = min(len(st) for st in strs)
        for i in range(l):
            for j in range(len(strs)-1):
                if strs[j][i] != strs[j+1][i]:
                    return "".join(ans)
            ans.append(strs[0][i])
        return "".join(ans)