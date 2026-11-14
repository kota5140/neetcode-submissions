class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for st in strs:
            encoded.append(str(len(st))+":"+st)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != ":":
                j += 1
            length = int("".join(s[i:j]))
            ans.append("".join(s[j+1:j+length+1]))
            i = j + length + 1

        return ans