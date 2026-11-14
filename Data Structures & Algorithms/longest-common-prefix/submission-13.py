class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = []
        for st in zip(*strs):
            if len(set(st)) > 1:
                break
            ans.append(st[0])
        return "".join(ans)