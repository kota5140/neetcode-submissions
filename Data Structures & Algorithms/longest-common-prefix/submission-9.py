class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ans = []
        strss = sorted(strs)
        first, last = strss[0], strss[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                break
            ans.append(first[i])
        return "".join(ans)