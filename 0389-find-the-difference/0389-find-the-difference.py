from collections import Counter

class Solution:
    def findTheDifference(self, s, t):
        count = Counter(t)

        for ch in s:
            count[ch] -= 1

        for ch in count:
            if count[ch] > 0:
                return ch
        