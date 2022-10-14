# Longest Substring Without Repeating Characters

#EN
# Given a string s, find the length of the longest substring without repeating characters.

#RU
# Для заданной строки s найдите длину самой длинной подстроки без повторяющихся символов.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = set()
        i = ans = 0
        for j, c in enumerate(s):
            while c in ss:
                ss.remove(s[i])
                i += 1
            ss.add(c)
            ans = max(ans, j - i + 1)
        return ans