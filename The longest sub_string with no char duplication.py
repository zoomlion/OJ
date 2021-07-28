# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        occ = set()
        n = len(s)

        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                occ.remove(s[i-1]) # no duplication
            while rk < n-1 and s[rk + 1] not in occ:
                occ.add(s[rk + 1])
                rk += 1
            ans = max(ans, rk - i + 1)
        return ans